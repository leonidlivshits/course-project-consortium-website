import json
import logging
from io import StringIO
from unittest.mock import patch

import pytest
from flask import Flask
from sqlalchemy.exc import IntegrityError

from app.logging_config import HANDLER_NAME, JsonFormatter, configure_logging
from app.routes import send_email


@pytest.fixture
def app_log_output(app_testing):
    handler = next(
        item for item in app_testing.logger.handlers
        if item.name == HANDLER_NAME
    )
    output = StringIO()
    previous_stream = handler.stream
    handler.setStream(output)
    try:
        yield output
    finally:
        handler.setStream(previous_stream)


def log_entries(output):
    return [json.loads(line) for line in output.getvalue().splitlines()]


def application_entries(output):
    return [
        entry for entry in log_entries(output)
        if entry["event"] != "http.request.completed"
    ]


def test_log_without_event_uses_default_name():
    record = logging.LogRecord(
        "app", logging.INFO, __file__, 1, "message", (), None
    )

    entry = json.loads(JsonFormatter().format(record))

    assert entry["event"] == "application.log"


def test_invalid_log_level_keeps_existing_handlers():
    app = Flask("invalid_log_level_test")
    app.config["LOG_LEVEL"] = "INVALID"
    handlers = list(app.logger.handlers)

    with pytest.raises(ValueError, match="LOG_LEVEL"):
        configure_logging(app)

    assert app.logger.handlers == handlers


def test_missing_recipient_log_excludes_contact_data(
    client, app_testing, app_log_output, mock_contact_data
):
    app_testing.config["SMTP_TO"] = None

    response = client.post("/api/contact", json=mock_contact_data)

    assert response.status_code == 503
    entries = application_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.smtp_unconfigured"
    assert entries[0]["level"] == "ERROR"
    assert all(
        value not in app_log_output.getvalue()
        for value in mock_contact_data.values()
    )


def test_invalid_email_log_excludes_address(
    client, app_log_output, mock_contact_data
):
    invalid_data = mock_contact_data | {"email": "private@@example.com"}

    response = client.post("/api/contact", json=invalid_data)

    assert response.status_code == 400
    entries = application_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.invalid_email"
    assert entries[0]["level"] == "WARNING"
    assert invalid_data["email"] not in app_log_output.getvalue()


def test_database_error_log_excludes_sql_parameters(
    client, app_log_output, mock_contact_data
):
    secret = "private@example.com"
    failure = IntegrityError(
        "INSERT INTO contact (email) VALUES (%(email)s)",
        {"email": secret},
        Exception("constraint failed"),
    )
    with patch("app.routes.db.session.commit", side_effect=failure):
        response = client.post("/api/contact", json=mock_contact_data)

    assert response.status_code == 500
    entries = application_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.database_write_failed"
    assert entries[0]["error.type"] == "IntegrityError"
    assert secret not in app_log_output.getvalue()


def test_email_delivery_log_excludes_exception_and_recipient(app_log_output):
    with patch("app.routes.mail") as mail:
        mail.send.side_effect = RuntimeError("private@example.com")
        result = send_email(
            "Subject", "from@example.com", ["to@example.com"], "Body"
        )

    assert result is False
    entries = log_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.email_delivery_failed"
    assert entries[0]["error.type"] == "RuntimeError"
    assert "private@example.com" not in app_log_output.getvalue()
    assert "to@example.com" not in app_log_output.getvalue()


def test_email_delivery_failure_is_logged_once(
    client, app_log_output, mock_contact_data
):
    failure = RuntimeError("private@example.com")
    with patch("app.routes.mail.send", side_effect=failure):
        response = client.post("/api/contact", json=mock_contact_data)

    assert response.status_code == 500
    assert "сохранено, но не отправлено" in response.get_json()["error"]
    entries = application_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.email_delivery_failed"
    assert "private@example.com" not in app_log_output.getvalue()


def test_email_processing_log_excludes_exception(
    client, app_log_output, mock_contact_data
):
    failure = RuntimeError("private@example.com")
    with patch("app.routes.send_email", side_effect=failure):
        response = client.post("/api/contact", json=mock_contact_data)

    assert response.status_code == 500
    entries = application_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.email_processing_failed"
    assert entries[0]["error.type"] == "RuntimeError"
    assert "private@example.com" not in app_log_output.getvalue()


def test_http_request_log_uses_route_template_and_omits_query(
    client, app_log_output
):
    response = client.get("/api/events/987654?token=private-token")

    assert response.status_code == 404
    entries = log_entries(app_log_output)
    assert len(entries) == 1
    entry = entries[0]
    assert entry["event"] == "http.request.completed"
    assert entry["level"] == "INFO"
    assert entry["http.request.method"] == "GET"
    assert entry["http.route"] == "/api/events/<int:event_id>"
    assert entry["http.response.status_code"] == 404
    assert entry["duration_ms"] >= 0
    assert "private-token" not in app_log_output.getvalue()
    assert "/api/events/987654" not in app_log_output.getvalue()


def test_http_request_log_covers_unmatched_and_successful_routes(
    client, app_log_output
):
    missing_response = client.get("/missing?token=private-token")
    health_response = client.get("/api/health")

    assert missing_response.status_code == 404
    assert health_response.status_code == 204
    entries = log_entries(app_log_output)
    assert len(entries) == 2
    assert entries[0]["http.route"] == "<unmatched>"
    assert entries[0]["http.response.status_code"] == 404
    assert entries[1]["http.route"] == "/api/health"
    assert entries[1]["http.response.status_code"] == 204
    assert "private-token" not in app_log_output.getvalue()
