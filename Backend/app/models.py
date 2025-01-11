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