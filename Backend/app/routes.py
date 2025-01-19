

# Последняя рабочая версия

from flask import Blueprint, request, jsonify
from .models import db, Contact, Event, Project, News, Publications, Organisation
from flask_mail import Message
from . import mail

main = Blueprint('main', __name__)

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

@main.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    projects_list = []
    for project in projects:
        projects_list.append({
            'id': project.id,
            'title': project.title,
            'authors': project.authors,
            'publication_date': project.publication_date,
            'description': project.description,
            'content': project.content,
            'materials': project.materials
        })
    return jsonify(projects_list), 200

@main.route('/api/news', methods=['GET'])
def get_news():
    news_1 = News.query.all()
    news_list = []
    for news in news_1:
        news_list.append({
            'id': news.id,
            'title': news.title,
            'authors': news.authors,
            'publication_date': news.publication_date,
            'description': news.description,
            'magazine': news.magazine,
            'content': news.content,
            'materials': news.materials
        })
    return jsonify(news_list), 200


@main.route('/api/publications', methods=['GET'])
def get_publications():
    publications_1 = Publications.query.all()
    publications_list = []
    for publication in publications_1:
        publications_list.append({
            'id': publication.id,
            'title': publication.title,
            'authors': publication.authors,
            'publication_date': publication.publication_date,
            'magazine': publication.magazine,
            'annotation': publication.annotation
        })
    return jsonify(publications_list), 200

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
