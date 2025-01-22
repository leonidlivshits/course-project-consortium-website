
     
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import LargeBinary

# db = SQLAlchemy()

# # Таблица для журналов
# class Magazine(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False, unique=True)  # Уникальное название журнала
#     news = db.relationship('News', backref='magazine', cascade="all, delete")
#     publications = db.relationship('Publications', backref='magazine', cascade="all, delete")

# # Таблица для авторов
# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)  # Имя
#     last_name = db.Column(db.String(50), nullable=False)   # Фамилия
#     middle_name = db.Column(db.String(50), nullable=True)  # Отчество (может быть NULL)

# # Таблица связи для новостей и авторов
# news_authors = db.Table('news_authors',
#     db.Column('news_id', db.Integer, db.ForeignKey('news.id', ondelete="CASCADE"), primary_key=True),
#     db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete="CASCADE"), primary_key=True)
# )

# # Таблица связи для публикаций и авторов
# publication_authors = db.Table('publication_authors',
#     db.Column('publication_id', db.Integer, db.ForeignKey('publications.id', ondelete="CASCADE"), primary_key=True),
#     db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete="CASCADE"), primary_key=True)
# )

# # Промежуточная таблица для проектов и авторов
# project_authors = db.Table('project_authors',
#     db.Column('project_id', db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"), primary_key=True),
#     db.Column('author_id', db.Integer, db.ForeignKey('author.id', ondelete="CASCADE"), primary_key=True)
# )
# # Модель для контактов
# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)
#     company = db.Column(db.String(100))
#     message = db.Column(db.Text, nullable=False)

# # Модель для событий
# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.String(50), nullable=False)
#     time = db.Column(db.String(50), nullable=False)
#     location = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=False)

# # Модель для новостей
# class News(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     publication_date = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id', ondelete="CASCADE"), nullable=True)
#     content = db.Column(db.Text, nullable=False)
#     materials = db.Column(db.Text)
#     authors = db.relationship('Author', secondary=news_authors, lazy='subquery',
#                               backref=db.backref('news', lazy=True), cascade="all, delete")

# # Модель для публикаций
# class Publications(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     publication_date = db.Column(db.String(50), nullable=False)
#     magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id', ondelete="CASCADE"), nullable=True)
#     annotation = db.Column(db.Text, nullable=False)
#     authors = db.relationship('Author', secondary=publication_authors, lazy='subquery',
#                               backref=db.backref('publications', lazy=True), cascade="all, delete")

# # Модель для проектов
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     publication_date = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     #materials = db.Column(db.Text)
#     materials = db.Column(LargeBinary)  # Для хранения файлов в базе данных
#     # или
#     #materials = db.Column(db.String(500))  # Для хранения пути к файлу на сервере
#     authors = db.relationship('Author', secondary=project_authors, lazy='subquery',
#                               backref=db.backref('projects', lazy=True), cascade="all, delete")


# # Модель для организаций
# class Organisation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.String(200), nullable=False)
#     link = db.Column(db.String(200), nullable=False)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Таблица для журналов
class Magazine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # Уникальное название журнала
    news = db.relationship('News', backref='magazine', cascade="all, delete")
    publications = db.relationship('Publications', backref='magazine', cascade="all, delete")

# Таблица для авторов
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)  # Имя
    last_name = db.Column(db.String(50), nullable=False)   # Фамилия
    middle_name = db.Column(db.String(50), nullable=True)  # Отчество (может быть NULL)

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

# Модель для событий
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Модель для новостей
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id', ondelete="CASCADE"), nullable=True)
    content = db.Column(db.Text, nullable=False)
    materials = db.Column(db.String(200))  # Путь к файлу
    authors = db.relationship('Author', secondary=news_authors, lazy='subquery',
                              backref=db.backref('news', lazy=True), cascade="all, delete")

# Модель для публикаций
class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.String(50), nullable=False)
    magazine_id = db.Column(db.Integer, db.ForeignKey('magazine.id', ondelete="CASCADE"), nullable=True)
    annotation = db.Column(db.Text, nullable=False)
    authors = db.relationship('Author', secondary=publication_authors, lazy='subquery',
                              backref=db.backref('publications', lazy=True), cascade="all, delete")

# Модель для проектов
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    materials = db.Column(db.String(200))  # Путь к файлу
    authors = db.relationship('Author', secondary=project_authors, lazy='subquery',
                              backref=db.backref('projects', lazy=True), cascade="all, delete")

# Модель для организаций
class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)