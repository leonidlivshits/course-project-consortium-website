# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_mail import Mail
# # from .config import Config
# # from .models import db
# # from flask_cors import CORS

# # mail = Mail()

# # def create_app():
# #     app = Flask(__name__)
# #     app.config.from_object(Config)
# #     app.config['DEBUG'] = True
# #     db.init_app(app)
# #     mail.init_app(app)
    
# #     CORS(app, origins = ["http://localhost:3000", "http://127.0.0.1:3000"])
# #     # Регистрация Blueprint
# #     from .routes import main
# #     app.register_blueprint(main)

# #     with app.app_context():
# #         db.create_all()

# #     return app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail
# from flask_migrate import Migrate  # Импортируем Migrate
# from .config import Config
# from .models import db
# from flask_cors import CORS

# mail = Mail()
# migrate = Migrate()  # Создаём объект Migrate

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     app.config['DEBUG'] = True
#     db.init_app(app)
#     mail.init_app(app)
#     migrate.init_app(app, db)  # Инициализируем Migrate
    
#     CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
    
#     # Регистрация Blueprint
#     from .routes import main
#     app.register_blueprint(main)

#     with app.app_context():
#         db.create_all()  # Создаём таблицы, если их нет

#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
import logging

# Настройка логгера
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Инициализация расширений
db = SQLAlchemy()
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

    # Регистрация Blueprint
    from .routes import main
    app.register_blueprint(main)

    # Добавление ModelView для Flask-Admin
    from .models import Magazine, Author, Contact, Event, News, Publications, Project, Organisation
    try:
        admin.add_view(ModelView(Magazine, db.session, name='Magazines', category='Models', endpoint='unique_magazine_admin'))
        admin.add_view(ModelView(Author, db.session, name='Authors', category='Models', endpoint='unique_author_admin'))
        admin.add_view(ModelView(Contact, db.session, name='Contacts', category='Models', endpoint='unique_contact_admin'))
        admin.add_view(ModelView(Event, db.session, name='Events', category='Models', endpoint='unique_event_admin'))
        admin.add_view(ModelView(News, db.session, name='News', category='Models', endpoint='unique_news_admin'))
        admin.add_view(ModelView(Publications, db.session, name='Publications', category='Models', endpoint='unique_publications_admin'))
        admin.add_view(ModelView(Project, db.session, name='Projects', category='Models', endpoint='unique_project_admin'))
        admin.add_view(ModelView(Organisation, db.session, name='Organisations', category='Models', endpoint='unique_organisation_admin'))
    except ValueError as e:
        logger.error(f"Error adding view: {e}")
        raise

    CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

    with app.app_context():
        db.create_all()  # Создаём таблицы, если их нет

    return app