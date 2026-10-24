from prometheus_client import Counter


class BusinessMetrics:
    def __init__(self, registry):
        self.news_views = Counter(
            "consortium_news_views_total",
            "Successful news detail views",
            registry=registry,
        )
        self.publication_views = Counter(
            "consortium_publication_views_total",
            "Successful publication detail views",
            registry=registry,
        )
        self.searches = Counter(
            "consortium_searches_total",
            "Successful searches",
            registry=registry,
        )
        self.contacts_saved = Counter(
            "consortium_contacts_saved_total",
            "Contacts saved to the database",
            registry=registry,
        )
