from flask import Blueprint, request, jsonify, send_from_directory, Response
from werkzeug.utils import secure_filename
import os
from .models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author
from flask_mail import Message
from . import mail
from . import serializers
main = Blueprint('main', __name__)

UPLOADS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
os.makedirs(UPLOADS_DIR, exist_ok=True)

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
        news_list.append(serializers.serialize_news(news))
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
            'authors': [serializers.serialize_author(author) 
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


@main.route('/api/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    event = Event.query.get(event_id)
    if event:
        return jsonify({
            'id': event.id,
            'title': event.title,
            'date': event.date,
            'time': event.time,
            'location': event.location,
            'description': event.description
        }), 200
    else:
        return jsonify({'error': 'Событие не найдено'}), 404


@main.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    project = Project.query.get(project_id)
    if project:
        return jsonify({
            'id': project.id,
            'title': project.title,
            'publication_date': project.publication_date,
            'description': project.description,
            'content': project.content,
            'materials': project.materials,
            'authors': [f"{author.last_name} {author.first_name[0]}." for author in project.authors]
        }), 200
    else:
        return jsonify({'error': 'Проект не найден'}), 404


# @main.route('/api/search', methods=['GET'])
# def search():
#     query = request.args.get('q', '').strip()
    
#     if not query:
#         return jsonify({"error": "Пустой запрос"}), 400

#     # Используем ILIKE для поиска подстроки без учета регистра
#     search_pattern = f"%{query}%"

#     # Выполняем поиск по всем таблицам
#     news_results = News.query.filter(News.title.ilike(search_pattern)).all()
#     publications_results = Publications.query.filter(Publications.title.ilike(search_pattern)).all()
#     projects_results = Project.query.filter(Project.title.ilike(search_pattern)).all()
#     events_results = Event.query.filter(Event.title.ilike(search_pattern)).all()
#     organisations_results = Organisation.query.filter(Organisation.link.ilike(search_pattern)).all()

#     # Формируем JSON-ответ
#     results = {
#         "news": [{"id": n.id, "title": n.title} for n in news_results],
#         "publications": [{"id": p.id, "title": p.title} for p in publications_results],
#         "projects": [{"id": pr.id, "title": pr.title} for pr in projects_results],
#         "events": [{"id": e.id, "title": e.title} for e in events_results],
#         "organisations": [{"id": o.id, "link": o.link} for o in organisations_results],
#     }

#     return jsonify(results)






# if __name__ == '__main__':
#     app.run(debug=True)


@main.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()

    print(f" Получен запрос на поиск: '{query}'")

    if not query:
        return jsonify({"error": "Пустой запрос"}), 400

    search_pattern = f"%{query}%"  # Поиск подстроки
    #search_pattern = query
    # Поиск по названиям и содержимому
    news_results = News.query.filter(
        (News.title.ilike(search_pattern)) | 
        (News.description.ilike(search_pattern)) | 
        (News.content.ilike(search_pattern))
    ).all()

    publications_results = Publications.query.filter(
        (Publications.title.ilike(search_pattern)) | 
        (Publications.annotation.ilike(search_pattern))
    ).all()

    projects_results = Project.query.filter(
        (Project.title.ilike(search_pattern)) | 
        (Project.description.ilike(search_pattern)) | 
        (Project.content.ilike(search_pattern))
    ).all()

    events_results = Event.query.filter(
        (Event.title.ilike(search_pattern)) | 
        (Event.description.ilike(search_pattern)) | 
        (Event.location.ilike(search_pattern))
    ).all()

    organisations_results = Organisation.query.filter(
        (Organisation.link.ilike(search_pattern))
    ).all()

    # Поиск по авторам (имя, фамилия, отчество)
    authors_results = Author.query.filter(
        (Author.first_name.ilike(search_pattern)) | 
        (Author.last_name.ilike(search_pattern)) | 
        (Author.middle_name.ilike(search_pattern))
    ).all()

    # Поиск по журналам
    magazines_results = Magazine.query.filter(
        Magazine.name.ilike(search_pattern)
    ).all()

    # Формируем JSON-ответ
    results = {
        "news": [{"id": n.id, "title": n.title} for n in news_results],
        "publications": [{"id": p.id, "title": p.title} for p in publications_results],
        "projects": [{"id": pr.id, "title": pr.title, "link" : f"/events/{pr.id}"} for pr in projects_results],
        "events": [{"id": e.id, "title": e.title, "link" : f"/events/{e.id}"} for e in events_results],
        "organisations": [{"id": o.id, "link": o.link} for o in organisations_results],
        "authors": [{"id": a.id, "name": f"{a.last_name} {a.first_name} {a.middle_name or ''}".strip()} for a in authors_results],
        "magazines": [{"id": m.id, "name": m.name} for m in magazines_results]
    }

    return jsonify(results)