from prometheus_client import CollectorRegistry
from prometheus_flask_exporter import PrometheusMetrics

from .business_metrics import BusinessMetrics


def configure_metrics(app):
    registry = CollectorRegistry()
    app.extensions["business_metrics"] = BusinessMetrics(registry)
    PrometheusMetrics(
        app,
        registry=registry,
        group_by="url_rule",
    )
