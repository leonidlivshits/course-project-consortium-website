from unittest.mock import patch

from prometheus_client.parser import text_string_to_metric_families
from sqlalchemy.exc import IntegrityError

from app.models import Contact


BUSINESS_METRICS = (
    "consortium_news_views_total",
    "consortium_publication_views_total",
    "consortium_searches_total",
    "consortium_contacts_saved_total",
)


def _business_values(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    samples = [
        sample
        for family in text_string_to_metric_families(response.get_data(as_text=True))
        for sample in family.samples
        if sample.name in BUSINESS_METRICS
    ]
    assert len(samples) == len(BUSINESS_METRICS)
    assert all(sample.labels == {} for sample in samples)
    return {sample.name: sample.value for sample in samples}


def test_http_metrics_include_status_and_duration(client):
    assert client.get("/api/events").status_code == 200
    assert client.get("/api/news/999999").status_code == 404

    response = client.get("/metrics")
    assert response.status_code == 200

    samples = [
        sample
        for family in text_string_to_metric_families(response.get_data(as_text=True))
        for sample in family.samples
    ]

    def sample_value(name, **labels):
        return next(
            sample.value
            for sample in samples
            if sample.name == name and sample.labels == labels
        )

    assert sample_value("flask_http_request_total", method="GET", status="200") == 1
    assert sample_value("flask_http_request_total", method="GET", status="404") == 1
    assert sample_value(
        "flask_http_request_duration_seconds_count",
        method="GET",
        url_rule="/api/events",
        status="200",
    ) == 1
    assert sample_value(
        "flask_http_request_duration_seconds_sum",
        method="GET",
        url_rule="/api/events",
        status="200",
    ) >= 0


def test_detail_views_count_only_existing_records(client, route_news, route_publication):
    expected = dict.fromkeys(BUSINESS_METRICS, 0)
    assert _business_values(client) == expected

    assert client.get(f"/api/news/{route_news.id}").status_code == 200
    expected["consortium_news_views_total"] = 1
    assert _business_values(client) == expected

    assert client.get(f"/api/publications/{route_publication.id}").status_code == 200
    expected["consortium_publication_views_total"] = 1
    assert _business_values(client) == expected

    assert client.get("/api/news/999999").status_code == 404
    assert client.get("/api/publications/999999").status_code == 404
    assert _business_values(client) == expected
    assert _business_values(client) == expected


def test_search_counts_success_without_results(client):
    expected = dict.fromkeys(BUSINESS_METRICS, 0)
    assert client.get("/api/search?q=").status_code == 400
    assert _business_values(client) == expected

    assert client.get("/api/search?q=absent-term").status_code == 200
    expected["consortium_searches_total"] = 1
    assert _business_values(client) == expected
    assert _business_values(client) == expected


def test_contact_counts_successful_save(client_mail, mock_contact_data):
    with patch("app.routes.send_email", return_value=True):
        assert client_mail.post("/api/contact", json=mock_contact_data).status_code == 201
    assert _business_values(client_mail)["consortium_contacts_saved_total"] == 1


def test_contact_counts_database_save_even_if_email_fails(client_mail, mock_contact_data):
    expected = dict.fromkeys(BUSINESS_METRICS, 0)
    with patch("app.routes.db.session.commit") as commit:
        commit.side_effect = IntegrityError("INSERT INTO contact", {}, Exception("failed"))
        assert client_mail.post("/api/contact", json=mock_contact_data).status_code == 500
    assert _business_values(client_mail) == expected

    with patch("app.routes.send_email", return_value=False):
        assert client_mail.post("/api/contact", json=mock_contact_data).status_code == 500
    assert Contact.query.count() == 1
    expected["consortium_contacts_saved_total"] = 1
    assert _business_values(client_mail) == expected

    assert client_mail.post("/api/contact", json=mock_contact_data).status_code == 409
    assert _business_values(client_mail) == expected
    assert _business_values(client_mail) == expected
