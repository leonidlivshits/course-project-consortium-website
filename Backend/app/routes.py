

# # Последняя рабочая версия

# from flask import Blueprint, request, jsonify
# from .models import db, Contact, Event, Project, News, Publications, Organisation
# from flask_mail import Message
# from . import mail

# main = Blueprint('main', __name__)

# @main.route('/api/contact', methods=['POST'])
# def create_contact():
#     print("create_contact --------------------------------------")
#     data = request.get_json()
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

# @main.route('/api/projects', methods=['GET'])
# def get_projects():
#     projects = Project.query.all()
#     projects_list = []
#     for project in projects:
#         projects_list.append({
#             'id': project.id,
#             'title': project.title,
#             'authors': project.authors,
#             'publication_date': project.publication_date,
#             'description': project.description,
#             'content': project.content,
#             'materials': project.materials
#         })
#     return jsonify(projects_list), 200

# @main.route('/api/news', methods=['GET'])
# def get_news():
#     news_1 = News.query.all()
#     news_list = []
#     for news in news_1:
#         news_list.append({
#             'id': news.id,
#             'title': news.title,
#             'authors': news.authors,
#             'publication_date': news.publication_date,
#             'description': news.description,
#             'magazine': news.magazine,
#             'content': news.content,
#             'materials': news.materials
#         })
#     return jsonify(news_list), 200


# @main.route('/api/publications', methods=['GET'])
# def get_publications():
#     publications_1 = Publications.query.all()
#     publications_list = []
#     for publication in publications_1:
#         publications_list.append({
#             'id': publication.id,
#             'title': publication.title,
#             'authors': publication.authors,
#             'publication_date': publication.publication_date,
#             'magazine': publication.magazine,
#             'annotation': publication.annotation
#         })
#     return jsonify(publications_list), 200

# @main.route('/api/organisations', methods=['GET'])
# def get_organisations():
#     organisations_1 = Organisation.query.all()
#     organisations_list = []
#     for organisation in organisations_1:
#         organisations_list.append({
#             'id': organisation.id,
#             'image': organisation.image,
#             'link': organisation.link
#         })
#     return jsonify(organisations_list), 200



# from flask import Blueprint, request, jsonify
# from .models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author
# from flask_mail import Message
# from . import mail
# from werkzeug.utils import secure_filename
# import os
# from flask import Response
# main = Blueprint('main', __name__)

# # Маршрут для создания контакта
# @main.route('/api/contact', methods=['POST'])
# def create_contact():
#     print("create_contact --------------------------------------")
#     data = request.get_json()
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


# @main.route('/api/projects', methods=['POST'])
# def create_project():
#     data = request.form
#     file = request.files.get('materials')

#     new_project = Project(
#         title=data['title'],
#         publication_date=data['publication_date'],
#         description=data['description'],
#         content=data['content'],
#         materials=file.read() if file else None  # Сохраняем файл как бинарные данные
#     )

#     # Добавляем авторов (если переданы их ID)
#     author_ids = data.getlist('author_ids')
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
#         projects_list.append({
#             'id': project.id,
#             'title': project.title,
#             'authors': [f"{author.last_name} {author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}" 
#                         for author in project.authors],  # Форматирование авторов
#             'publication_date': project.publication_date,
#             'description': project.description,
#             'content': project.content,
#             'materials': project.materials
#         })
#     return jsonify(projects_list), 200



# @main.route('/api/projects/<int:project_id>/materials', methods=['GET'])
# #@cross_origin()
# def download_materials(project_id):
#     project = Project.query.get_or_404(project_id)
#     if not project.materials:
#         return jsonify({'message': 'Файл не найден'}), 404

#     return Response(
#         project.materials,
#         mimetype='application/octet-stream',
#         headers={'Content-Disposition': f'attachment; filename={project.title}.bin'}
#     )



# # Маршрут для получения всех новостей
# @main.route('/api/news', methods=['GET'])
# def get_news():
#     news_1 = News.query.all()
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
#             'materials': news.materials
#         })
#     return jsonify(news_list), 200

# # Маршрут для получения всех публикаций
# @main.route('/api/publications', methods=['GET'])
# def get_publications():
#     publications_1 = Publications.query.all()
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
#     organisations_1 = Organisation.query.all()
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
            'materials': news.materials
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