from sqlalchemy import Column, Integer
from wtforms import Form
from flask_mail import Mail
from unittest.mock import MagicMock, patch
from pytest import fixture
from datetime import datetime, date, time
import sys
from pathlib import Path
from sqlalchemy.exc import SQLAlchemyError
from flask_admin import Admin

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from app.models import (
    Author,
    News,
    Event,
    Project,
    Publications,
    Organisation,
    Magazine,
    Contact,
    db,
)

from app import (
    create_app,
    CustomQuerySelectField,
    MyModelView,
    MyQuerySelectMultipleField
)


@fixture
def sample_author_with_middle_name():
    return Author(
        id=1,
        last_name="Иванов",
        first_name="Иван",
        middle_name="Иванович",
    )


@fixture
def sample_author_without_middle_name():
    return Author(
        id=2,
        last_name="Петров",
        first_name="Петр",
        middle_name=None,
    )


@fixture
def sample_magazine():
    return Magazine(id=1, name="Журнал 1")


@fixture
def sample_news(sample_author_with_middle_name, sample_author_without_middle_name, sample_magazine):
    news = News(
        id=1,
        title="Новость 1",
        publication_date=date(2023, 10, 1),
        description="Описание новости 1",
        magazine=sample_magazine,
        content="Контент новости 1",
        materials="kitchen.jpg",
    )
    news.authors.extend([sample_author_with_middle_name, sample_author_without_middle_name])
    return news


@fixture
def sample_event():
    return Event(
        id=1,
        title="Событие 1",
        publication_date=date(2023, 10, 1),
        location="Москва",
        description="Описание события 1",
    )


@fixture
def sample_project(sample_author_with_middle_name):
    project = Project(
        id=1,
        title="Проект 1",
        publication_date=date(2023, 9, 1),
        description="Описание проекта 1",
        content="Контент проекта 1",
        materials="loqiemean-как-у-людеи.mp3",
    )
    project.authors.extend([sample_author_with_middle_name])
    return project


@fixture
def sample_publication(sample_author_with_middle_name, sample_author_without_middle_name, sample_magazine):
    publication = Publications(
        id=1,
        title="Публикация 1",
        publication_date=date(2023, 8, 1),
        annotation="Аннотация публикации 1",
    )
    publication.authors.extend([sample_author_with_middle_name, sample_author_without_middle_name])
    publication.magazine = sample_magazine
    return publication


@fixture
def sample_organisation():
    return Organisation(
        id=1,
        image="kitchen.jpg",
        link="https://t.me/vyshkochka1",
    )
@fixture
def sample_contact():
    return Contact(
        id = 1,
        name = "Leo Livshitz",
        email = "maxweinsberg@gmail.com",
        phone = "89444557578",
        company = "Lego",
        message = "message"
    )

@fixture
def app_testing():
    app = create_app("app.config.TestConfig")
    with app.app_context():
        try:
            db.create_all()
            yield app
        finally:
            db.session.remove()
            db.drop_all()


@fixture
def client(app_testing):
    return app_testing.test_client()



@fixture
def route_organisation():
    org = Organisation(image="image1.png", link="https://org1.com")
    db.session.add(org)
    db.session.commit()
    return db.session.get(Organisation, org.id)




@fixture
def route_event():
    event = Event(
        title="Event1",
        description="Description1",
        publication_date=date(2023, 10, 1),
        location="Location1",
    )
    db.session.add(event)
    db.session.commit()
    return db.session.get(Event, event.id)


@fixture
def route_news():
    news = News(
        title="News1",
        description="Description1",
        publication_date=datetime(2023, 10, 1),
        content="Content1",
    )
    db.session.add(news)
    db.session.commit()
    return db.session.get(News, news.id)


@fixture
def route_project():
    project = Project(
        title="Project1",
        description="Description1",
        publication_date=datetime(2023, 10, 1),
        content="Content1",
    )
    db.session.add(project)
    db.session.commit()
    return db.session.get(Project, project.id)


@fixture
def route_publication():
    publication = Publications(
        title="Publication1",
        annotation="Annotation1",
        publication_date=datetime(2023, 10, 1),
    )
    db.session.add(publication)
    db.session.commit()
    return db.session.get(Publications, publication.id)


@fixture
def route_author():
    author = Author(first_name="Leo", last_name="Livshitz")
    db.session.add(author)
    db.session.commit()
    return db.session.get(Author, author.id)


@fixture
def route_magazine():
    magazine = Magazine(name="Magazine1")
    db.session.add(magazine)
    db.session.commit()
    return db.session.get(Magazine, magazine.id)


@fixture
def mock_contact_data():
    return {
        "name": "Test Contact",
        "email": "leonidlivshits05@gmail.com",
        "phone": "9876543210",
        "message": "This is a test message"
    }


@fixture(autouse=True)
def auto_mock_translator(monkeypatch):
    mock_translate = lambda text, translator=None: f"{text}_en"
    monkeypatch.setattr("app.translator.translate_to_english", mock_translate)



@fixture
def uploaded_organisation(sample_organisation):
    org = sample_organisation
    db.session.add(org)
    db.session.commit()
    return db.session.get(Organisation, org.id)

class MockMail:
    def init_app(app, *args, **kwargs):
        pass

@fixture
def app_testing_mail():
    app = create_app("app.config.TestConfig", MockMail())
    with app.app_context():
        try:
            db.create_all()
            yield app
        finally:
            db.session.remove()
            db.drop_all()


@fixture
def client_mail(app_testing_mail):
    return app_testing_mail.test_client()



@fixture
def create_form_with_field_helper():
    def _create_form_with_field(field_class, **kwargs):
        class TestForm(Form):
            test_field = field_class("Test", **kwargs)
        return TestForm
    return _create_form_with_field

@fixture
def dummy_query_factory():
    return lambda: [Author(id=1, first_name="John", last_name="Doe")]
