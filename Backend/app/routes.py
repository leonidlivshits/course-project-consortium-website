# from flask import Blueprint, request, jsonify
# from app.models import db, Contact
# from flask_mail import Message
# from Backend import mail


# main = Blueprint('main', __name__)

# @main.route('/api/contact', methods=['POST'])
# def create_contact():
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

#     # Отправка письма
#     msg = Message(
#         subject='Новое сообщение от ' + data['name'],
#         sender=data['email'],  # Используем email из формы как отправителя
#         recipients=['maxweinsberg25@gmail.com'],  # Ваша почта
#         body=f"Имя: {data['name']}\nEmail: {data['email']}\nТелефон: {data['phone']}\nКомпания: {data.get('company')}\nСообщение: {data['message']}"
#     )
#     mail.send(msg)

#     return jsonify({'message': 'Сообщение отправлено успешно!'}), 201

# from flask import Blueprint, request, jsonify
# from .models import db, Contact
# from flask_mail import Message
# from app import mail

# from flask import Blueprint, request, jsonify
# from app.models import db, Contact
# from flask_mail import Message
# from app import mail


# main = Blueprint('main', __name__)

# @main.route('/api/contact', methods=['POST'])
# def create_contact():
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

#     # Отправка письма
#     msg = Message(
#         subject='Новое сообщение от ' + data['name'],
#         sender=data['email'],  # Используем email из формы как отправителя
#         recipients=['maxweinsberg25@gmail.com'],  # Ваша почта
#         body=f"Имя: {data['name']}\nEmail: {data['email']}\nТелефон: {data['phone']}\nКомпания: {data.get('company')}\nСообщение: {data['message']}"
#     )
#     mail.send(msg)

#     return jsonify({'message': 'Сообщение отправлено успешно!'}), 201


# from flask import Blueprint, request, jsonify
# from .models import db, Contact
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

# Последняя рабочая версия

from flask import Blueprint, request, jsonify
from .models import db, Contact, Event, Project
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
