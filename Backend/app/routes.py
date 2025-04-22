from sqlite3 import IntegrityError
from flask import Blueprint, request, jsonify, send_from_directory, Response, session
from email_validator import validate_email, EmailNotValidError
from sqlalchemy import select as sa_select
from werkzeug.utils import secure_filename
import os
from .models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author
from flask_mail import Message
from . import mail
from . import serializers
#from .utils import get_current_language
import logging
from datetime import datetime
from enum import Enum, auto
from sqlalchemy import or_
main = Blueprint('main', __name__)

# UPLOADS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
# os.makedirs(UPLOADS_DIR, exist_ok=True)

BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOADS_DIR = os.path.join(BASEDIR, 'uploads')
os.makedirs(UPLOADS_DIR, exist_ok=True)

from flask_mail import Message

# Маршрут для отдачи файлов
@main.route('/api/uploads/<filename>')
def uploaded_file(filename):
    print(UPLOADS_DIR)
    return send_from_directory(UPLOADS_DIR, filename)

# @main.route('/api/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400
    
#     filename = secure_filename(file.filename)
#     save_path = os.path.join(UPLOADS_DIR, filename)
    
#     # Быстрая потоковая запись
#     with open(save_path, 'wb') as f:
#         chunk_size = 4096
#         while True:
#             chunk = file.stream.read(chunk_size)
#             if not chunk:
#                 break
#             f.write(chunk)
    
#     return jsonify({
#         "url": f"/api/uploads/{filename}",
#         "message": "File uploaded successfully"
#     }), 201

def send_email(subject, sender, recipients, body):
    try:
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = body
        mail.send(msg)
        return True
    except Exception as e:
        logging.error(f"Ошибка при отправке email: {e}")
        return False



@main.route('/api/contact', methods=['POST'])
def create_contact():
    #print("create_contact --------------------------------------")
    data = request.get_json()

    # Проверка обязательных полей
    if not all(key in data for key in ['name', 'email', 'phone', 'message']):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Валидация email
        email_info = validate_email(data['email'], check_deliverability=False)
        normalized_email = email_info.normalized
    except EmailNotValidError as e:
        logging.error(f"Email validation error: {e}")
        return jsonify({'error': 'Invalid email address'}), 400

    # Проверка на существующую запись
    existing_contact = Contact.query.filter_by(
        email=normalized_email,
        message=data['message']
    ).first()

    if existing_contact:
        return jsonify({'error': 'Сообщение с этого email уже отправлено'}), 409

    try:
        new_contact = Contact(
            name=data['name'],
            email=normalized_email,
            phone=data['phone'],
            company=data.get('company'),
            message=data['message']
        )
        
        db.session.add(new_contact)
        db.session.commit()

    except IntegrityError as e:
        db.session.rollback()
        logging.error(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

    # Отправка email
    try:
        subject = f'Новое сообщение от {data["name"]}'
        body = f"""Имя: {data['name']}
Email: {normalized_email}
Телефон: {data['phone']}
Компания: {data.get('company', 'не указано')}
Сообщение: {data['message']}"""
        
        if send_email(subject, normalized_email, ['admin@dobhdvfc.mailosaur.net'], body):
            return jsonify({'message': 'Сообщение отправлено успешно!'}), 201
        else:
            raise Exception('Email sending failed')

    except Exception as e:
        logging.error(f"Email sending error: {e}")
        return jsonify({'error': 'Сообщение сохранено, но не отправлено'}), 500

# @main.route('/api/contact', methods=['POST'])
# def create_contact():
#     print("create_contact --------------------------------------")
#     data = request.get_json()

#     # Проверка валидности email
#     try:
#         email_info = validate_email(data['email'], check_deliverability=False)
#         data['email'] = email_info.normalized
#     except EmailNotValidError as e:
#         logging.error(f"Email validation error: {e}")
#         return jsonify({'error': 'Invalid email address provided.'}), 400
#     except IntegrityError as e:
#         db.session.rollback()
#         logging.error(f"Duplicate entry: {e}")
#         return jsonify({'error': 'Сообщение с этого email уже отправлено'}), 409
#     except Exception as e:
#         db.session.rollback()
#         logging.error(f"Error: {e}")
#         return jsonify({'error': 'Internal server error'}), 500

#     new_contact = Contact(
#         name=data['name'],
#         email=data['email'],
#         phone=data['phone'],
#         company=data.get('company'),
#         message=data['message']
#     )
#     db.session.add(new_contact)
#     db.session.commit()

#     # Отправка email
#     subject = f'Новое сообщение от {data["name"]}'
#     body = f"Имя: {data['name']}\nEmail: {data['email']}\nТелефон: {data['phone']}\nКомпания: {data.get('company')}\nСообщение: {data['message']}"
#     if send_email(subject, data['email'], ['maxweinsberg25@gmail.com'], body):
#         return jsonify({'message': 'Сообщение отправлено успешно!'}), 201
#     else:
#         return jsonify({'error': 'Не удалось отправить сообщение'}), 200


# Маршрут для получения всех событий
@main.route('/api/events', methods=['GET'])
def get_events():
    events = db.session.scalars(sa_select(Event)).all()  # ЗАМЕНА: query.all() -> session.scalars(select(...)).all()
    events_list = []
    for event in events:
        events_list.append(serializers.serialize_events(event))
    return jsonify(events_list), 200


# Маршрут для получения события по ID
@main.route('/api/events/<int:event_id>', methods=['GET'])  # Добавил <int:event_id> для корректного маршрута
def get_event_by_id(event_id):
    event = db.session.get(Event, event_id)  # ЗАМЕНА: query.get() -> session.get()
    if event:
        return jsonify(serializers.serialize_events(event)), 200
    else:
        return jsonify({'error': 'Событие не найдено'}), 404


# Маршрут для получения всех проектов
@main.route('/api/projects', methods=['GET'])
def get_projects():
    projects = db.session.scalars(sa_select(Project)).all()  # ЗАМЕНА: query.all() -> session.scalars(select(...)).all()
    projects_list = []
    for project in projects:
        projects_list.append(serializers.serialize_projects(project))
    return jsonify(projects_list), 200


# Маршрут для получения проекта по ID
@main.route('/api/projects/<int:project_id>', methods=['GET'])  # Добавил <int:project_id> для корректного маршрута
def get_project_by_id(project_id):
    project = db.session.get(Project, project_id)  # ЗАМЕНА: query.get() -> session.get()
    if project:
        return jsonify(serializers.serialize_projects(project)), 200
    else:
        return jsonify({'error': 'Проект не найден'}), 404


# Маршрут для получения всех новостей
@main.route('/api/news', methods=['GET'])
def get_news():
    all_news = db.session.scalars(sa_select(News)).all()
    news_list = []
    for news in all_news:
        news_list.append(serializers.serialize_news(news))
    return jsonify(news_list), 200


# Маршрут для получения новости по ID
@main.route('/api/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    news = db.session.get(News, news_id)
    if news:
        return jsonify(serializers.serialize_news(news)), 200
    else:
        return jsonify({'error': 'Новость не найдена'}), 404


# Маршрут для получения всех публикаций
@main.route('/api/publications', methods=['GET'])
def get_publications():
    all_publications = db.session.scalars(sa_select(Publications)).all() 
    publications_list = []
    for publication in all_publications:
        publications_list.append(serializers.serialize_publications(publication))
    return jsonify(publications_list), 200


# Маршрут для получения публикации по ID
@main.route('/api/publications/<int:publication_id>', methods=['GET'])  # Добавил <int:publication_id> для корректного маршрута
def get_publication_by_id(publication_id):
    publication = db.session.get(Publications, publication_id)  # ЗАМЕНА: query.get() -> session.get()
    if publication:
        return jsonify(serializers.serialize_publications(publication)), 200
    else:
        return jsonify({'error': 'Публикация не найдена'}), 404


# Маршрут для получения всех организаций
@main.route('/api/organisations', methods=['GET'])
#@basic_auth.required
def get_organisations():
    all_organisations = db.session.scalars(sa_select(Organisation)).all()  # ЗАМЕНА: query.all() -> session.scalars(select(...)).all()
    organisations_list = []
    for organisation in all_organisations:
        organisations_list.append(serializers.serialize_organisations(organisation))
    return jsonify(organisations_list), 200


# Маршрут для получения организации по ID
@main.route('/api/organisations/<int:organisation_id>', methods=['GET'])  # Добавил <int:organisation_id> для корректного маршрута
def get_organisation_by_id(organisation_id):
    organisation = db.session.get(Organisation, organisation_id)  # ЗАМЕНА: query.get() -> session.get()
    if organisation:
        return jsonify(serializers.serialize_organisations(organisation)), 200
    else:
        return jsonify({'error': 'Организация не найдена'}), 404




@main.route('/api/magazines/<int:magazine_id>', methods=['GET']) 
def get_magazine_by_id(magazine_id):
    magazine = db.session.get(Magazine, magazine_id) 
    if magazine:
        return jsonify(serializers.serialize_magazine(magazine)), 200
    else:
        return jsonify({'error': 'магазин не найден'}), 404


@main.route('/api/magazines', methods=['GET'])
def get_magazines():
    magazines = db.session.scalars(sa_select(Magazine)).all()
    magazines_list = [serializers.serialize_magazine(mag) for mag in magazines]
    return jsonify(magazines_list), 200

@main.route('/api/authors/<int:author_id>', methods=['GET']) 
def get_author_by_id(author_id):
    author = db.session.get(Author, author_id) 
    if author:
        return jsonify(serializers.serialize_author(author)), 200
    else:
        return jsonify({'error': 'автор не найден'}), 404

@main.route('/api/authors', methods=['GET'])
def get_authors():
    authors = db.session.scalars(sa_select(Author)).all() 
    authors_list = [serializers.serialize_author(author) for author in authors]
    return jsonify(authors_list), 200




def get_and_sort_results(model, filters, sort_key=None, reverse=False):
    results = db.session.scalars(sa_select(model).filter(*filters)).all()
    if sort_key:
        results = sorted(results, key=lambda x: getattr(x, sort_key), reverse=reverse)
    return results

class SortType(Enum):
    ALPHABETICAL = auto()  # Сортировка по алфавиту
    REVERSE_ALPHABETICAL = auto()  # Сортировка в обратном алфавитном порядке
    DATE_ASC = auto()  # Сортировка по дате (по возрастанию)
    DATE_DESC = auto()  # Сортировка по дате (по убыванию)

def get_sort_params(sort_type):
    sort_mapping = {
        SortType.ALPHABETICAL: {"sort_key": "title", "reverse": False},
        SortType.REVERSE_ALPHABETICAL: {"sort_key": "title", "reverse": True},
        SortType.DATE_ASC: {"sort_key": "publication_date", "reverse": False},
        SortType.DATE_DESC: {"sort_key": "publication_date", "reverse": True},
    }
    return sort_mapping.get(sort_type, {"sort_key": None, "reverse": False})

def build_text_filters(model, fields, search_pattern):

    filters = []
    
    for field in fields:
        if hasattr(model, field):
            filters.append(getattr(model, field).ilike(search_pattern))

        en_field = f"{field}_en"
        if hasattr(model, en_field):
            filters.append(getattr(model, en_field).ilike(search_pattern))
    
    return or_(*filters) if filters else None



def build_filters(query, authors, magazines, date_from, date_to):
    word_pattern = f"%{query}%"
    
    filters = {
        "news": [],
        "publications": [],
        "events": [],
        "projects": [],
        "organisations": [],
        "magazines": [],
        "authors": [],
    }

    filters["news"].append(build_text_filters(News, ['title', 'description', 'content'], word_pattern))
    filters["publications"].append(build_text_filters(Publications, ['title', 'annotation'], word_pattern))
    filters["events"].append(build_text_filters(Event, ['title', 'description', 'location'], word_pattern))
    filters["projects"].append(build_text_filters(Project, ['title', 'description', 'content'], word_pattern))
    filters["organisations"].append(Organisation.link.ilike(word_pattern))

    filters["magazines"].append(build_text_filters(Magazine, ['name'], word_pattern))
    filters["authors"].append(build_text_filters(Author, ['first_name', 'last_name', 'middle_name'], word_pattern))

    if authors:
        filters["news"].append(News.authors.any(Author.id.in_(authors)))
        filters["publications"].append(Publications.authors.any(Author.id.in_(authors)))
        filters["projects"].append(Project.authors.any(Author.id.in_(authors)))

    if magazines:
        filters["news"].append(News.magazine_id.in_(magazines))
        filters["publications"].append(Publications.magazine_id.in_(magazines))

    if date_from and date_to:
        filters["news"].append(News.publication_date.between(date_from, date_to))
        filters["publications"].append(Publications.publication_date.between(date_from, date_to))
        filters["events"].append(Event.publication_date.between(date_from, date_to))
        filters["projects"].append(Project.publication_date.between(date_from, date_to))

    return filters


@main.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    sort_type_str = request.args.get('sort', '').strip()
    authors = [int(a) for a in request.args.getlist('authors[]') if a.strip().isdigit()]
    magazines = [int(m) for m in request.args.getlist('magazines[]') if m.strip().isdigit()]
    date_from = request.args.get('date_from', type=lambda x: datetime.strptime(x, '%Y-%m-%d') if x else None)
    date_to = request.args.get('date_to', type=lambda x: datetime.strptime(x, '%Y-%m-%d') if x else None)

    if not query:
        return jsonify({"error": "Пустой запрос"}), 400

    try:
        sort_type = SortType[sort_type_str.upper()]
    except KeyError:
        sort_type = None

    sort_params = get_sort_params(sort_type)
    sort_key = sort_params["sort_key"]
    reverse = sort_params["reverse"]
    search_pattern = query #f"%{query}%"

    # Получаем базовые фильтры через отдельную функцию
    base_filters = build_filters(search_pattern, authors, magazines, date_from, date_to)

    # Получение результатов с использованием корректных фильтров
    news_results = get_and_sort_results(News, base_filters["news"], sort_key=sort_key, reverse=reverse)
    publications_results = get_and_sort_results(Publications, base_filters["publications"], sort_key=sort_key, reverse=reverse)
    events_results = get_and_sort_results(Event, base_filters["events"], sort_key=sort_key, reverse=reverse)
    projects_results = get_and_sort_results(Project, base_filters["projects"], sort_key=sort_key, reverse=reverse)
    organisations_results = db.session.scalars(sa_select(Organisation).filter(*base_filters["organisations"])).all()

    # Сбор авторов и журналов из найденных записей
    # authors_results = set()
    # magazines_results = set()

    # for news in news_results:
    #     authors_results.update(news.authors)
    #     if news.magazine:
    #         magazines_results.add(news.magazine)

    # for publication in publications_results:
    #     authors_results.update(publication.authors)
    #     if publication.magazine:
    #         magazines_results.add(publication.magazine)

    # for project in projects_results:
    #     authors_results.update(project.authors)

    authors_results = []
    magazines_results = []

    for news in news_results:
        authors_results.extend(news.authors)
        if news.magazine:
            magazines_results.append(news.magazine)

    for publication in publications_results:
        authors_results.extend(publication.authors)
        if publication.magazine:
            magazines_results.append(publication.magazine)

    for project in projects_results:
        authors_results.extend(project.authors)

    results = {
        "news": [{"id": n.id, "title": n.title, "title_en": n.title_en, "link": f"/news/{n.id}"} for n in news_results],
        "publications": [{"id": p.id, "title": p.title, "title_en": p.title_en,"link": f"/publications/{p.id}"} for p in publications_results],
        "projects": [{"id": pr.id, "title": pr.title, "title_en": pr.title_en,"link": f"/projects/{pr.id}"} for pr in projects_results],
        "events": [{"id": e.id, "title": e.title, "title_en": e.title_en, "link": f"/events/{e.id}"} for e in events_results],
        "organisations": [{"id": o.id, "link": f"/organisations/{o.id}"} for o in organisations_results],
        # "authors": [{"id": a.id, "name": f"{a.last_name} {a.first_name} {a.middle_name or ''}".strip()} for a in authors_results],
        # "magazines": [{"id": m.id, "name": m.name} for m in magazines_results]
    }

    return jsonify(results)
