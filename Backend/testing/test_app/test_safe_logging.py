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
    entries = log_entries(app_log_output)
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
    entries = log_entries(app_log_output)
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
    entries = log_entries(app_log_output)
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
    entries = log_entries(app_log_output)
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
    entries = log_entries(app_log_output)
    assert len(entries) == 1
    assert entries[0]["event"] == "contact.email_processing_failed"
    assert entries[0]["error.type"] == "RuntimeError"
    assert "private@example.com" not in app_log_output.getvalue()
