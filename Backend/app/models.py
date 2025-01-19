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
    title = db.Column(db.String(100), nullable=False)
    authors = db.Column(db.String(200), nullable=False)  
    publication_date = db.Column(db.String(50), nullable=False) 
    description = db.Column(db.Text, nullable=False) 
    content = db.Column(db.Text, nullable=False)  
    materials = db.Column(db.Text)  
    
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) 
    authors = db.Column(db.String(200), nullable=False)  
    publication_date = db.Column(db.String(50), nullable=False) 
    description = db.Column(db.Text, nullable=False)  
    magazine = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=False)  
    materials = db.Column(db.Text)  

class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  
    authors = db.Column(db.String(200), nullable=False)  
    publication_date = db.Column(db.String(50), nullable=False)  
    magazine = db.Column(db.String(100), nullable=True)
    annotation = db.Column(db.Text, nullable=False)  
    
