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
from flask import Blueprint, request, jsonify
from .models import db, Contact
from flask_mail import Message
from . import mail

main = Blueprint('main', __name__)

@main.route('/api/contact', methods=['POST'])
def create_contact():
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