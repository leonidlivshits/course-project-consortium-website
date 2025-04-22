import datetime
from unittest.mock import patch
from app.serializers import (
    serialize_author,
    serialize_news,
    serialize_events,
    serialize_projects,
    serialize_publications,
    serialize_organisations
)

class TestAuthorSerializer:
    def test_serialize_author_with_middle_name(self, sample_author_with_middle_name):
        result = serialize_author(sample_author_with_middle_name)
        assert result == {
            'id' : 1,
            'first_name': 'Иван',
            'first_name_en': None,
            'last_name': 'Иванов',
            'last_name_en': None,
            'middle_name': 'Иванович',
            'middle_name_en': None
        }
        
    def test_serialize_author_without_middle_name(self, sample_author_without_middle_name):
        result = serialize_author(sample_author_without_middle_name)
        assert result == {
            'id' : 2,
            'first_name': 'Петр',
            'first_name_en': None,
            'last_name': 'Петров',
            'last_name_en': None,
            'middle_name': None,
            'middle_name_en': None
        }


class TestNewsSerializer:
    @patch("app.utils.get_current_language", return_value="ru")
    def test_serialize_news_with_magazine(self, mock_get_current_language, sample_news):
        result = serialize_news(sample_news)
        
        expected_authors = [
            {
                'id' : 1,
                'first_name': 'Иван', 
                'first_name_en': None,
                'last_name': 'Иванов',
                'last_name_en': None,
                'middle_name': 'Иванович',
                'middle_name_en': None
            },
            {
                'id' : 2,
                'first_name': 'Петр',
                'first_name_en': None,
                'last_name': 'Петров',
                'last_name_en': None,
                'middle_name': None,
                'middle_name_en': None
            }
        ]
        assert result["authors"] == expected_authors
        
    @patch("app.utils.get_current_language", return_value="ru")
    def test_serialize_news_without_magazine(self, mock_get_current_language, sample_news):
        sample_news.magazine = None
        result = serialize_news(sample_news)
        assert result["magazine"] is None


    

class TestPublicationSerializer:
    @patch("app.utils.get_current_language", return_value="ru")
    def test_serialize_publication_authors(self, mock_get_current_language, sample_publication):
        result = serialize_publications(sample_publication)
        authors_ids = [author["id"] for author in result["authors"]]
        assert set(authors_ids) == {1, 2}

class TestEventSerializer:
    @patch("app.utils.get_current_language", return_value="ru")
    def test_serialize_event_time_format(self, mock_get_current_language, sample_event):
        result = serialize_events(sample_event)
        assert result["publication_date"] == datetime.date(2023, 10, 1)


class TestProjectSerializer:
    @patch("app.utils.get_current_language", return_value="ru")
    def test_serialize_project_materials(self, mock_get_current_language, sample_project):
        result = serialize_projects(sample_project)
        assert result["materials"] == "/uploads/loqiemean-как-у-людеи.mp3"


class TestOrganisationSerializer:
    def test_serialize_organisation(self, sample_organisation):
        result = serialize_organisations(sample_organisation)
        
        assert result["id"] == 1
        assert result["image"] == "kitchen.jpg"
        assert result["link"] == "https://t.me/vyshkochka1"

