from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_admin import Admin
from flask_cors import CORS
import logging
from .models import db
from .config import Config
from .admin_views import register_admin_views  # Импорт функции

# Инициализация расширений
#db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
admin = Admin(name='Admin Panel', template_mode='bootstrap3')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['DEBUG'] = True

    # Инициализация расширений
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    # Регистрация представлений Flask-Admin
    register_admin_views(admin, db)  # Вызов функции

    # Регистрация Blueprint
    from .routes import main
    app.register_blueprint(main)

    CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

    with app.app_context():
        db.create_all()

    return app