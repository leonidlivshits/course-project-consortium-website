# from flask import Blueprint, request, jsonify, send_from_directory, Response, current_app
# from werkzeug.utils import secure_filename
# import os
# from flask_mail import Message

# main = Blueprint('main', __name__)

# # Папка для загрузки файлов
# UPLOADS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
# os.makedirs(UPLOADS_DIR, exist_ok=True)  # Создаем папку, если она не существует

# # Маршрут для создания контакта
# @main.route('/api/contact', methods=['POST'])
# def create_contact():
#     print("create_contact --------------------------------------")
#     data = request.get_json()

#     # Получаем объекты db и mail из контекста приложения
#     db = current_app.extensions['sqlalchemy'].db
#     mail = current_app.extensions['mail']

#     new_contact = current_app.models.Contact(
#         name=data['name'],
#         email=data['email'],
#         phone=data['phone'],
#         company=data.get('company'),
#         message=data['message']
#     )
#     db.session.add(new_contact)
#     db.session.commit()

#     msg = Message(
#         subject=f'Новое сообщение от {data["name"]}',
#         sender=data['email'],
#         recipients=['maxweinsberg25@gmail.com'],
#         body=f"Имя: {data['name']}\nEmail: {data['email']}\nТелефон: {data['phone']}\nКомпания: {data.get('company')}\nСообщение: {data['message']}"
#     )
#     mail.send(msg)

#     return jsonify({'message': 'Сообщение отправлено успешно!'}), 201

# # Маршрут для получения всех событий
# @main.route('/api/events', methods=['GET'])
# def get_events():
#     db = current_app.extensions['sqlalchemy'].db
#     events = db.session.query(current_app.models.Event).all()
#     events_list = []
#     for event in events:
#         events_list.append({
#             'id': event.id,
#             'title': event.title,
#             'date': event.date,
#             'time': event.time,
#             'location': event.location,
#             'description': event.description
#         })
#     return jsonify(events_list), 200

# # Маршрут для создания проекта
# @main.route('/api/projects', methods=['POST'])
# def create_project():
#     if 'materials' not in request.files:
#         return jsonify({'error': 'Файл не найден'}), 400

#     file = request.files['materials']
#     if file.filename == '':
#         return jsonify({'error': 'Файл не выбран'}), 400

#     # Сохраняем файл
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(UPLOADS_DIR, filename)
#     file.save(file_path)

#     # Получаем объект db из контекста приложения
#     db = current_app.extensions['sqlalchemy'].db

#     # Сохраняем путь к файлу в базе данных
#     new_project = current_app.models.Project(
#         title=request.form['title'],
#         publication_date=request.form['publication_date'],
#         description=request.form['description'],
#         content=request.form['content'],
#         materials=filename  # Сохраняем имя файла
#     )

#     # Добавляем авторов (если переданы их ID)
#     author_ids = request.form.getlist('author_ids')
#     for author_id in author_ids:
#         author = db.session.query(current_app.models.Author).get(author_id)
#         if author:
#             new_project.authors.append(author)

#     db.session.add(new_project)
#     db.session.commit()

#     return jsonify({'message': 'Проект успешно создан!'}), 201

# # Маршрут для получения всех проектов
# @main.route('/api/projects', methods=['GET'])
# def get_projects():
#     db = current_app.extensions['sqlalchemy'].db
#     projects = db.session.query(current_app.models.Project).all()
#     projects_list = []
#     for project in projects:
#         projects_list.append({
#             'id': project.id,
#             'title': project.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}." for author in project.authors],
#             'publication_date': project.publication_date,
#             'description': project.description,
#             'content': project.content,
#             'materials': f"/uploads/{project.materials}"  # Путь к файлу
#         })
#     return jsonify(projects_list), 200

# # Маршрут для отдачи файлов
# @main.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(UPLOADS_DIR, filename)

# # Маршрут для создания новости
# @main.route('/api/news', methods=['POST'])
# def create_news():
#     if 'materials' not in request.files:
#         return jsonify({'error': 'Файл не найден'}), 400

#     file = request.files['materials']
#     if file.filename == '':
#         return jsonify({'error': 'Файл не выбран'}), 400

#     # Сохраняем файл
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(UPLOADS_DIR, filename)
#     file.save(file_path)

#     # Получаем объект db из контекста приложения
#     db = current_app.extensions['sqlalchemy'].db

#     # Сохраняем путь к файлу в базе данных
#     new_news = current_app.models.News(
#         title=request.form['title'],
#         publication_date=request.form['publication_date'],
#         description=request.form['description'],
#         content=request.form['content'],
#         materials=filename  # Сохраняем имя файла
#     )

#     # Добавляем авторов (если переданы их ID)
#     author_ids = request.form.getlist('author_ids')
#     for author_id in author_ids:
#         author = db.session.query(current_app.models.Author).get(author_id)
#         if author:
#             new_news.authors.append(author)

#     # Добавляем журнал (если передан ID)
#     magazine_id = request.form.get('magazine_id')
#     if magazine_id:
#         magazine = db.session.query(current_app.models.Magazine).get(magazine_id)
#         if magazine:
#             new_news.magazine_id = magazine.id

#     db.session.add(new_news)
#     db.session.commit()

#     return jsonify({'message': 'Новость успешно создана!'}), 201

# # Маршрут для получения всех новостей
# @main.route('/api/news', methods=['GET'])
# def get_news():
#     db = current_app.extensions['sqlalchemy'].db
#     news_1 = db.session.query(current_app.models.News).all()
#     news_list = []
#     for news in news_1:
#         news_list.append({
#             'id': news.id,
#             'title': news.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
#                         for author in news.authors],
#             'publication_date': news.publication_date,
#             'description': news.description,
#             'magazine': news.magazine.name if news.magazine else None,
#             'content': news.content,
#             'materials': f"/uploads/{news.materials}"  # Путь к файлу
#         })
#     return jsonify(news_list), 200

# # Маршрут для получения всех публикаций
# @main.route('/api/publications', methods=['GET'])
# def get_publications():
#     db = current_app.extensions['sqlalchemy'].db
#     publications_1 = db.session.query(current_app.models.Publications).all()
#     publications_list = []
#     for publication in publications_1:
#         publications_list.append({
#             'id': publication.id,
#             'title': publication.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
#                         for author in publication.authors],
#             'publication_date': publication.publication_date,
#             'magazine': publication.magazine.name if publication.magazine else None,
#             'annotation': publication.annotation
#         })
#     return jsonify(publications_list), 200

# # Маршрут для получения всех организаций
# @main.route('/api/organisations', methods=['GET'])
# def get_organisations():
#     db = current_app.extensions['sqlalchemy'].db
#     organisations_1 = db.session.query(current_app.models.Organisation).all()
#     organisations_list = []
#     for organisation in organisations_1:
#         organisations_list.append({
#             'id': organisation.id,
#             'image': organisation.image,
#             'link': organisation.link
#         })
#     return jsonify(organisations_list), 200

# # Маршрут для получения всех журналов
# @main.route('/api/magazines', methods=['GET'])
# def get_magazines():
#     db = current_app.extensions['sqlalchemy'].db
#     magazines = db.session.query(current_app.models.Magazine).all()
#     magazines_list = [{'id': mag.id, 'name': mag.name} for mag in magazines]
#     return jsonify(magazines_list), 200

# # Маршрут для получения всех авторов
# @main.route('/api/authors', methods=['GET'])
# def get_authors():
#     db = current_app.extensions['sqlalchemy'].db
#     authors = db.session.query(current_app.models.Author).all()
#     authors_list = [{'id': author.id, 'first_name': author.first_name, 
#                      'last_name': author.last_name, 'middle_name': author.middle_name} 
#                     for author in authors]
#     return jsonify(authors_list), 200



# from flask import Blueprint, request, jsonify, send_from_directory, Response, current_app
# from werkzeug.utils import secure_filename
# import os
# from datetime import datetime
# from flask_mail import Message
# from app.models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author  # Импортируем модели и db напрямую
# from datetime import datetime

# main = Blueprint('main', __name__)

# # Папка для загрузки файлов
# UPLOADS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
# os.makedirs(UPLOADS_DIR, exist_ok=True)  # Создаем папку, если она не существует

# # Маршрут для создания контакта
# @main.route('/api/contact', methods=['POST'])
# def create_contact():
#     print("create_contact --------------------------------------")
#     data = request.get_json()

#     # Получаем объект mail из контекста приложения
#     mail = current_app.extensions['mail']

#     new_contact = Contact(
#         name=data['name'],
#         email=data['email'],
#         phone=data['phone'],
#         company=data.get('company'),
#         message=data['message']
#     )
#     db.session.add(new_contact)
#     db.session.commit()

#     msg = Message(
#         subject=f'Новое сообщение от {data["name"]}',
#         sender=data['email'],
#         recipients=['maxweinsberg25@gmail.com'],
#         body=f"Имя: {data['name']}\nEmail: {data['email']}\nТелефон: {data['phone']}\nКомпания: {data.get('company')}\nСообщение: {data['message']}"
#     )
#     mail.send(msg)

#     return jsonify({'message': 'Сообщение отправлено успешно!'}), 201

# # Маршрут для получения всех событий
# @main.route('/api/events', methods=['GET'])
# def get_events():
#     events = Event.query.all()
#     events_list = []
#     for event in events:
#         events_list.append({
#             'id': event.id,
#             'title': event.title,
#             'date': event.date,
#             'time': event.time,
#             'location': event.location,
#             'description': event.description
#         })
#     return jsonify(events_list), 200

# from datetime import datetime

# @main.route('/api/projects', methods=['POST'])
# def create_project():
#     if 'materials' not in request.files:
#         return jsonify({'error': 'Файл не найден'}), 400

#     file = request.files['materials']
#     if file.filename == '':
#         return jsonify({'error': 'Файл не выбран'}), 400

#     # Сохраняем файл
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(UPLOADS_DIR, filename)
#     file.save(file_path)

#     # Преобразуем строку в datetime
#     publication_date = datetime.strptime(request.form['publication_date'], "%d/%m/%y %H:%M")

#     # Сохраняем путь к файлу в базе данных
#     new_project = Project(
#         title=request.form['title'],
#         publication_date=publication_date,  # Используем объект datetime
#         description=request.form['description'],
#         content=request.form['content'],
#         materials=filename  # Сохраняем имя файла
#     )

#     # Добавляем авторов (если переданы их ID)
#     author_ids = request.form.getlist('author_ids')
#     for author_id in author_ids:
#         author = Author.query.get(author_id)
#         if author:
#             new_project.authors.append(author)

#     db.session.add(new_project)
#     db.session.commit()

#     return jsonify({'message': 'Проект успешно создан!'}), 201

# @main.route('/api/projects', methods=['GET'])
# def get_projects():
#     projects = Project.query.all()
#     projects_list = []
#     for project in projects:
#         # Проверяем тип данных publication_date
#         if isinstance(project.publication_date, str):
#             # Если это строка, преобразуем в datetime
#             from datetime import datetime
#             try:
#                 publication_date = datetime.strptime(project.publication_date, "%d/%m/%y %H:%M")
#             except ValueError:
#                 publication_date = None
#         else:
#             publication_date = project.publication_date

#         projects_list.append({
#             'id': project.id,
#             'title': project.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}." for author in project.authors],
#             'publication_date': publication_date.strftime("%d/%m/%y %H:%M") if publication_date else None,
#             'description': project.description,
#             'content': project.content,
#             'materials': f"/uploads/{project.materials}"  # Путь к файлу
#         })
#     return jsonify(projects_list), 200

# # Маршрут для отдачи файлов
# @main.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(UPLOADS_DIR, filename)

# from datetime import datetime

# @main.route('/api/news', methods=['POST'])
# def create_news():
#     if 'materials' not in request.files:
#         return jsonify({'error': 'Файл не найден'}), 400

#     file = request.files['materials']
#     if file.filename == '':
#         return jsonify({'error': 'Файл не выбран'}), 400

#     # Сохраняем файл
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(UPLOADS_DIR, filename)
#     file.save(file_path)

#     # Преобразуем строку в datetime
#     publication_date = datetime.strptime(request.form['publication_date'], "%d/%m/%y %H:%M")

#     # Сохраняем путь к файлу в базе данных
#     new_news = News(
#         title=request.form['title'],
#         publication_date=publication_date,  # Используем объект datetime
#         description=request.form['description'],
#         content=request.form['content'],
#         materials=filename  # Сохраняем имя файла
#     )

#     # Добавляем авторов (если переданы их ID)
#     author_ids = request.form.getlist('author_ids')
#     for author_id in author_ids:
#         author = Author.query.get(author_id)
#         if author:
#             new_news.authors.append(author)

#     # Добавляем журнал (если передан его ID)
#     magazine_id = request.form.get('magazine_id')
#     if magazine_id:
#         magazine = Magazine.query.get(magazine_id)
#         if magazine:
#             new_news.magazine_id = magazine.id

#     db.session.add(new_news)
#     db.session.commit()

#     return jsonify({'message': 'Новость успешно создана!'}), 201

# @main.route('/api/news', methods=['GET'])
# def get_news():
#     news_1 = News.query.all()
#     news_list = []
#     for news in news_1:
#         # Проверяем тип данных publication_date
#         if isinstance(news.publication_date, str):
#             # Если это строка, преобразуем в datetime
#             from datetime import datetime
#             try:
#                 publication_date = datetime.strptime(news.publication_date, "%d/%m/%y %H:%M")
#             except ValueError:
#                 publication_date = None
#         else:
#             publication_date = news.publication_date

#         news_list.append({
#             'id': news.id,
#             'title': news.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
#                         for author in news.authors],
#             'publication_date': publication_date.strftime("%d/%m/%y %H:%M") if publication_date else None,
#             'description': news.description,
#             'magazine': news.magazine.name if news.magazine else None,
#             'content': news.content,
#             'materials': f"/uploads/{news.materials}"  # Путь к файлу
#         })
#     return jsonify(news_list), 200
# @main.route('/api/publications', methods=['GET'])
# def get_publications():
#     publications_1 = Publications.query.all()
#     publications_list = []
#     for publication in publications_1:
#         # Проверяем тип данных publication_date
#         if isinstance(publication.publication_date, str):
#             # Если это строка, преобразуем в datetime
#             from datetime import datetime
#             try:
#                 publication_date = datetime.strptime(publication.publication_date, "%d/%m/%y %H:%M")
#             except ValueError:
#                 publication_date = None
#         else:
#             publication_date = publication.publication_date

#         publications_list.append({
#             'id': publication.id,
#             'title': publication.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
#                         for author in publication.authors],
#             'publication_date': publication_date.strftime("%d/%m/%y %H:%M") if publication_date else None,
#             'magazine': publication.magazine.name if publication.magazine else None,
#             'annotation': publication.annotation
#         })
#     return jsonify(publications_list), 200

# # Маршрут для получения всех организаций
# @main.route('/api/organisations', methods=['GET'])
# def get_organisations():
#     organisations = Organisation.query.all()
#     organisations_list = []
#     for organisation in organisations:
#         organisations_list.append({
#             'id': organisation.id,
#             'image': organisation.image,
#             'link': organisation.link
#         })
#     return jsonify(organisations_list), 200

# # Маршрут для получения всех журналов
# @main.route('/api/magazines', methods=['GET'])
# def get_magazines():
#     magazines = Magazine.query.all()
#     magazines_list = [{'id': mag.id, 'name': mag.name} for mag in magazines]
#     return jsonify(magazines_list), 200

# # Маршрут для получения всех авторов
# @main.route('/api/authors', methods=['GET'])
# def get_authors():
#     authors = Author.query.all()
#     authors_list = [{'id': author.id, 'first_name': author.first_name, 
#                      'last_name': author.last_name, 'middle_name': author.middle_name} 
#                     for author in authors]
#     return jsonify(authors_list), 200


from flask import Blueprint, request, jsonify, send_from_directory, Response
from werkzeug.utils import secure_filename
import os
from .models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author
from flask_mail import Message
from . import mail

main = Blueprint('main', __name__)

# Папка для загрузки файлов
#UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
UPLOADS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
os.makedirs(UPLOADS_DIR, exist_ok=True)  # Создаем папку, если она не существует

# Маршрут для создания контакта
@main.route('/api/contact', methods=['POST'])
def create_contact():
    print("create_contact --------------------------------------")
    data = request.get_json()
    new_contact = Contact(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        company=data.get('company'),
        message=data['message']
    )
    db.session.add(new_contact)
    db.session.commit()

    msg = Message(
        subject=f'Новое сообщение от {data["name"]}',
        sender=data['email'],
        recipients=['maxweinsberg25@gmail.com'],
        body=f"Имя: {data['name']}\nEmail: {data['email']}\nТелефон: {data['phone']}\nКомпания: {data.get('company')}\nСообщение: {data['message']}"
    )
    mail.send(msg)

    return jsonify({'message': 'Сообщение отправлено успешно!'}), 201

# Маршрут для получения всех событий
@main.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_list = []
    for event in events:
        events_list.append({
            'id': event.id,
            'title': event.title,
            'date': event.date,
            'time': event.time,
            'location': event.location,
            'description': event.description
        })
    return jsonify(events_list), 200

# Маршрут для создания проекта
@main.route('/api/projects', methods=['POST'])
def create_project():
    if 'materials' not in request.files:
        return jsonify({'error': 'Файл не найден'}), 400

    file = request.files['materials']
    if file.filename == '':
        return jsonify({'error': 'Файл не выбран'}), 400

    # Сохраняем файл
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOADS_DIR, filename)
    file.save(file_path)

    # Сохраняем путь к файлу в базе данных
    new_project = Project(
        title=request.form['title'],
        publication_date=request.form['publication_date'],
        description=request.form['description'],
        content=request.form['content'],
        materials=filename  # Сохраняем имя файла
    )

    # Добавляем авторов (если переданы их ID)
    author_ids = request.form.getlist('author_ids')
    for author_id in author_ids:
        author = Author.query.get(author_id)
        if author:
            new_project.authors.append(author)

    db.session.add(new_project)
    db.session.commit()

    return jsonify({'message': 'Проект успешно создан!'}), 201

# Маршрут для получения всех проектов
@main.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    projects_list = []
    for project in projects:
        projects_list.append({
            'id': project.id,
            'title': project.title,
            'authors': [f"{author.last_name} {author.first_name[0]}." for author in project.authors],
            'publication_date': project.publication_date,
            'description': project.description,
            'content': project.content,
            'materials': f"/uploads/{project.materials}"  # Путь к файлу
        })
    return jsonify(projects_list), 200

# Маршрут для отдачи файлов
@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOADS_DIR, filename)

@main.route('/api/news', methods=['POST'])
def create_news():
    if 'materials' not in request.files:
        return jsonify({'error': 'Файл не найден'}), 400

    file = request.files['materials']
    if file.filename == '':
        return jsonify({'error': 'Файл не выбран'}), 400

    # Сохраняем файл
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOADS_DIR, filename)
    file.save(file_path)

    # Сохраняем путь к файлу в базе данных
    new_news = News(
        title=request.form['title'],
        publication_date=request.form['publication_date'],
        description=request.form['description'],
        # magazine=request.form['magazine'],
        content=request.form['content'],
        materials=filename  # Сохраняем имя файла
    )

    # Добавляем авторов (если переданы их ID)
    author_ids = request.form.getlist('author_ids')
    for author_id in author_ids:
        author = Author.query.get(author_id)
        if author:
            new_news.authors.append(author)

    magazine = request.form.getlist('magazine')
    for magazine_id in magazine:
        magazine = Magazine.query.get(magazine_id)
        if magazine:
            new_news.magazine_id.append(magazine)

    db.session.add(new_news)
    db.session.commit()

    return jsonify({'message': 'Новость успешно создана!'}), 201

# Маршрут для получения всех новостей
@main.route('/api/news', methods=['GET'])
def get_news():
    news_1 = News.query.all()
    news_list = []
    for news in news_1:
        news_list.append({
            'id': news.id,
            'title': news.title,
            'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
                        for author in news.authors],
            'publication_date': news.publication_date,
            'description': news.description,
            'magazine': news.magazine.name if news.magazine else None,
            'content': news.content,
            'materials': f"/uploads/{news.materials}" #news.materials
        })
    return jsonify(news_list), 200

# Маршрут для получения всех публикаций
@main.route('/api/publications', methods=['GET'])
def get_publications():
    publications_1 = Publications.query.all()
    publications_list = []
    for publication in publications_1:
        publications_list.append({
            'id': publication.id,
            'title': publication.title,
            'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
                        for author in publication.authors],
            'publication_date': publication.publication_date,
            'magazine': publication.magazine.name if publication.magazine else None,
            'annotation': publication.annotation
        })
    return jsonify(publications_list), 200

# Маршрут для получения всех организаций
@main.route('/api/organisations', methods=['GET'])
def get_organisations():
    organisations_1 = Organisation.query.all()
    organisations_list = []
    for organisation in organisations_1:
        organisations_list.append({
            'id': organisation.id,
            'image': organisation.image,
            'link': organisation.link
        })
    return jsonify(organisations_list), 200

# Маршрут для получения всех журналов
@main.route('/api/magazines', methods=['GET'])
def get_magazines():
    magazines = Magazine.query.all()
    magazines_list = [{'id': mag.id, 'name': mag.name} for mag in magazines]
    return jsonify(magazines_list), 200

# Маршрут для получения всех авторов
@main.route('/api/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    authors_list = [{'id': author.id, 'first_name': author.first_name, 
                     'last_name': author.last_name, 'middle_name': author.middle_name} 
                    for author in authors]
    return jsonify(authors_list), 200