from prometheus_client.parser import text_string_to_metric_families


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
