# # from flask_sqlalchemy import SQLAlchemy

# # db = SQLAlchemy()
# from app import db
# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)
#     company = db.Column(db.String(80))
#     message = db.Column(db.Text, nullable=False)

#     # def __repr__(self):
#     #     return f"<Contact {self.name}>"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Название проекта
    authors = db.Column(db.String(200), nullable=False)  # Авторы (можно хранить как строку)
    publication_date = db.Column(db.String(50), nullable=False)  # Дата публикации
    description = db.Column(db.Text, nullable=False)  # Описание проекта
    content = db.Column(db.Text, nullable=False)  # Основной текст проекта
    materials = db.Column(db.Text)  # Материалы (например, ссылки или файлы)
