from prometheus_client import CollectorRegistry
from prometheus_flask_exporter import PrometheusMetrics


def configure_metrics(app):
    PrometheusMetrics(
        app,
        registry=CollectorRegistry(),
        group_by="url_rule",
    )
