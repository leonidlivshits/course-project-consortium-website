from dataclasses import field
from unittest.mock import MagicMock, patch
from sqlalchemy import Column, Integer, inspect
from wtforms import Form
from flask_admin.contrib.sqla import ModelView as BaseModelView
from app import create_app
from app.__init__ import CustomQuerySelectField, MyModelView, MyQuerySelectMultipleField
from app.config import TestConfig
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.form import FormMeta
import pytest
import base64
from flask import url_for
from app.models import (
    Organisation,
    Contact,
    Event,
    News,
    Project,
    Publications,
    Author,
    Magazine,
    db
)

class TestMyAdminIndexView:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client
        self.admin_url = '/admin/'
        self.valid_headers = self._auth_headers('admin', 'password')
        self.invalid_headers = self._auth_headers('wrong', 'wrong')

    def _auth_headers(self, username, password):
        credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
        return {'Authorization': f'Basic {credentials}'}

    def test_admin_access_without_auth(self):
        response = self.client.get(self.admin_url)
        assert response.status_code == 401
        assert 'WWW-Authenticate' in response.headers

    def test_admin_access_with_valid_auth(self):
        response = self.client.get(self.admin_url, headers=self.valid_headers)
        assert response.status_code == 200
        assert 'Admin Panel' in response.get_data(as_text=True)

    def test_admin_access_with_invalid_auth(self):
        response = self.client.get(self.admin_url, headers=self.invalid_headers)
        assert response.status_code == 401


class TestMyModelView:
    
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client
        self.valid_headers = self._auth_headers('admin', 'password')
        self.invalid_headers = self._auth_headers('wrong', 'wrong')
        self.endpoints = [
            '/admin/unique_magazine_admin/',
            '/admin/unique_author_admin/',
            '/admin/unique_contact_admin/',
            '/admin/unique_event_admin/',
            '/admin/unique_news_admin/',
            '/admin/unique_publications_admin/',
            '/admin/unique_project_admin/',
            '/admin/unique_organisation_admin/'
        ]

    def _auth_headers(self, username, password):
        credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
        return {'Authorization': f'Basic {credentials}'}

    @pytest.mark.parametrize("endpoint", [
        '/admin/unique_magazine_admin/',
        '/admin/unique_author_admin/',
        '/admin/unique_contact_admin/',
        '/admin/unique_event_admin/',
        '/admin/unique_news_admin/',
        '/admin/unique_publications_admin/',
        '/admin/unique_project_admin/',
        '/admin/unique_organisation_admin/'
    ])
    def test_model_view_access(self, endpoint):

        response = self.client.get(endpoint)
        assert response.status_code == 401

        response = self.client.get(endpoint, headers=self.valid_headers)
        assert response.status_code == 200


        response = self.client.get(endpoint, headers=self.invalid_headers)
        assert response.status_code == 401

    def test_all_model_views_in_sequence(self):
        for endpoint in self.endpoints:
            response = self.client.get(endpoint)
            assert response.status_code == 401
            
            response = self.client.get(endpoint, headers=self.valid_headers)
            assert response.status_code == 200
            
            response = self.client.get(endpoint, headers=self.invalid_headers)
            assert response.status_code == 401



def local_dummy_queryselectfield_init(self, label=None, validators=None, **kwargs):
    self.label = label
    self.validators = validators

    for key, value in kwargs.items():
        setattr(self, key, value)
    
    if not hasattr(self, "filters"):
        self.filters = []



class TestQuery:
    def test_custom_query_select_field_field_flags_conversion(
        self, app_testing, monkeypatch, create_form_with_field_helper, dummy_query_factory
    ):
        
        
        monkeypatch.setattr(QuerySelectField, "__init__", local_dummy_queryselectfield_init)
        
        FormClass = create_form_with_field_helper(
            CustomQuerySelectField,
            query_factory=dummy_query_factory,
            field_flags=("flag1", "flag2"),
            default=lambda: None
        )
        form = FormClass()
        field = form.test_field

        assert isinstance(field.field_flags, dict)
        assert field.field_flags.get("flag1") is True
        assert field.field_flags.get("flag2") is True

    def test_my_query_select_multiple_field_defaults(
        self, app_testing, monkeypatch, create_form_with_field_helper
    ):
        monkeypatch.setattr(QuerySelectField, "__init__", local_dummy_queryselectfield_init)
        FormClass = create_form_with_field_helper(
            MyQuerySelectMultipleField,
            default=lambda: []
        )
        form = FormClass()
        field = form.test_field

        with app_testing.app_context():
            query = field.query_factory()
        assert query is not None

        dummy_author = Author(id=1, first_name="John", last_name="Doe")
        label = field.get_label(dummy_author)
        assert label == "John Doe"
        pk = field.get_pk(dummy_author)
        assert pk == 1


def test_init_db_command():
    class EmptyDatabaseConfig(TestConfig):
        TESTING = False

    app = create_app(EmptyDatabaseConfig)
    with app.app_context():
        expected_tables = set(db.metadata.tables)
        assert not inspect(db.engine).get_table_names()

    result = app.test_cli_runner().invoke(args=['init-db'])

    assert result.exit_code == 0
    assert 'Таблицы созданы' in result.output
    with app.app_context():
        assert expected_tables.issubset(inspect(db.engine).get_table_names())
