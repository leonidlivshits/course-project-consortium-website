from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from .config import Config
from .models import db
from flask_cors import CORS

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['DEBUG'] = True
    db.init_app(app)
    mail.init_app(app)
    
    CORS(app, origins = ["http://localhost:3000", "http://127.0.0.1:3000"])
    # Регистрация Blueprint
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
