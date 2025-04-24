from sqlalchemy import UniqueConstraint
from . import utils
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time, date
from .translator import translate_to_english

db = SQLAlchemy()

class TranslateMixin:
    __translations__ = ()
    
    @classmethod
    def __declare_last__(cls):
        from sqlalchemy import event

        def translate_fields(mapper, connection, target):
            for from_field, to_field in target.__translations__:
                source_value = getattr(target, from_field)
                target_value = getattr(target, to_field)
                
                if source_value and not target_value:
                    translated = translate_to_english(source_value)
                    setattr(target, to_field, translated or source_value)

        event.listen(cls, 'before_insert', translate_fields)
        event.listen(cls, 'before_update', translate_fields)
        
        


# Таблица для журналов
class Magazine(TranslateMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    name_en = db.Column(db.String(100), nullable=True)
    news = db.relationship('News', backref='magazine', cascade="all, delete")
    publications = db.relationship('Publications', backref='magazine', cascade="all, delete")
    __translations__ = (
        ('name', 'name_en'),
    )
    def __str__(self):
        return self.name

# Таблица для авторов
class Author(TranslateMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    first_name_en = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    last_name_en = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    middle_name_en = db.Column(db.String(50), nullable=True)
    __translations__ = (
        ('first_name', 'first_name_en'),
        ('last_name', 'last_name_en'),
        ('middle_name', 'middle_name_en')
    )

# Таблица связи для новостей и авторов
news_authors = db.Table('news_authors',
    db.Column('news_id', db.Integer, db.ForeignKey('news.id', ondelete="CASCADE"), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete="CASCADE"), primary_key=True)
)

# Таблица связи для публикаций и авторов
publication_authors = db.Table('publication_authors',
    db.Column('publication_id', db.Integer, db.ForeignKey('publications.id', ondelete="CASCADE"), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete="CASCADE"), primary_key=True)
)

# Промежуточная таблица для проектов и авторов
project_authors = db.Table('project_authors',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete="CASCADE"), primary_key=True)
)

# Модель для контактов
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)

    __table_args__ = (
        UniqueConstraint('email', 'message', name='uq_email_message'),
    )

    def __str__(self):
        return (f"{self.id} {self.name}")


# Модель для событий
class Event(TranslateMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=True)
    publication_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    location_en = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=True)
    __translations__ = (
        ('title', 'title_en'),
        ('description', 'description_en'),
        ('location', 'location_en')
    )
    def __str__(self):
        return (f"{self.id} {self.title}")


# Модель для новостей
class News(TranslateMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=True)
    publication_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=True)
    magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id', ondelete="CASCADE"), nullable=True)
    content = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=True)
    materials = db.Column(db.String(300))
    authors = db.relationship('Author', secondary=news_authors, lazy='dynamic',
                              backref=db.backref('news', lazy=True), cascade="all, delete")
    __translations__ = (
        ('title', 'title_en'),
        ('description', 'description_en'),
        ('content', 'content_en')
    )
    def __str__(self):
        return (f"{self.id} {self.title}")

# Модель для публикаций
class Publications(TranslateMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=True)
    publication_date = db.Column(db.DateTime, nullable=False)
    magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id', ondelete="CASCADE"), nullable=True)
    annotation = db.Column(db.Text, nullable=False)
    annotation_en = db.Column(db.Text, nullable=True)
    authors = db.relationship('Author', secondary=publication_authors, lazy='dynamic',
                              backref=db.backref('publications', lazy=True), cascade="all, delete")
    __translations__ = (
        ('title', 'title_en'),
        ('annotation', 'annotation_en')
    )
    def __str__(self):
        return (f"{self.id} {self.title}")

# Модель для проектов
class Project(TranslateMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title_en = db.Column(db.String(100), nullable=True)
    publication_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text, nullable=True)
    materials = db.Column(db.String(300))
    authors = db.relationship('Author', secondary=project_authors, lazy='dynamic',
                              backref=db.backref('projects', lazy=True), cascade="all, delete")
    __translations__ = (
        ('title', 'title_en'),
        ('description', 'description_en'),
        ('content', 'content_en')
    )
    def __str__(self):
        return (f"{self.id} {self.title}")

# Модель для организаций
class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False, unique=True)
