from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
import logging
from .models import Author, Magazine, db
#from .admin_views import register_admin_views 
from flask_basicauth import BasicAuth
from flask import Response, redirect, Flask
from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView
#from flask_admin.contrib.fileadmin import FileAdmin
from .translator import translate_to_english
from werkzeug.exceptions import HTTPException
from wtforms import SelectMultipleField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.fields.core import Field

#import os



# Инициализация расширений
mail = Mail()
migrate = Migrate()
admin = Admin(name='Admin Panel', template_mode='bootstrap3')
basic_auth = BasicAuth()



# class AuthException(HTTPException):
#     def init(self, message):
#         super().init(message, Response(
#             "You could not be authenticated. Please refresh the page.", 401,
#             {'WWW-Authenticate': 'Basic realm="Login Required"'} ))

class CustomQuerySelectField(QuerySelectField):
    def __init__(self, *args, **kwargs):
        # Если передан параметр field_flags, и он — кортеж, преобразуем его в dict
        field_flags = kwargs.pop("field_flags", getattr(self, "field_flags", {}))
        if isinstance(field_flags, tuple):
            field_flags = {flag: True for flag in field_flags}
        kwargs["field_flags"] = field_flags
        super().__init__(*args, **kwargs)



class MyQuerySelectMultipleField(QuerySelectMultipleField):
    field_flags = {'query': True}

    def __init__(self, *args, **kwargs):
        if 'query_factory' not in kwargs:
            kwargs['query_factory'] = lambda: db.session.query(Author)
        if 'get_label' not in kwargs:
            kwargs['get_label'] = self.get_label  # Явно указываем метод get_label
        super().__init__(*args, **kwargs)



    def get_pk(self, obj):
        return obj.id

    def get_label(self, obj):
        return f"{obj.first_name} {obj.last_name}" 

class MyModelView(ModelView):
    # def scaffold_form(self):
    #     form_class = super().scaffold_form()
    #     if hasattr(form_class, '__translations__'):
    #         delattr(form_class, '__translations__')
    #     return form_class

    form_overrides = {
        'authors': MyQuerySelectMultipleField,
        'magazine': QuerySelectField
    }

    form_args = {

    'authors': {
        'query_factory': lambda: db.session.query(Author), 
        'get_label': lambda obj: f"{obj.first_name} {obj.last_name}"
    },
    'magazine': {
            'query_factory': lambda: db.session.query(Magazine),
            'get_label': 'name',
            'allow_blank': True
        }
}
    form_excluded_columns = ['__translations__']

    def is_accessible(self):
        return basic_auth.authenticate()
    
    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return basic_auth.authenticate()
    
    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()
    
# class MyFileAdmin(FileAdmin):
#     can_upload = True
#     can_delete = True
#     can_mkdir = False
#     allowed_extensions = ('pdf', 'jpg', 'png', 'docx')
    
#     def __init__(self):
#         upload_path = os.path.join(
#             os.path.dirname(os.path.dirname(__file__)), 
#             'uploads'
#         )
#         super().__init__(
#             base_path=upload_path,
#             url_prefix='/uploads',
#             name='Файлы',
#             category='Управление'
#         )
    
#     def is_accessible(self):
#         return basic_auth.authenticate()
    
#     def inaccessible_callback(self, name, **kwargs):
#         return basic_auth.challenge()


class NewsModelView(MyModelView):
    can_create = True

    form_ajax_refs = {
        'authors': {
            'fields': ['first_name', 'last_name'],
            'page_size': 10
        }
    }
    

class MagazineModelView(MyModelView):
    form_columns = ['name', 'name_en', 'news', 'publications']
    
def register_admin_views(admin: Admin, db):
    admin.add_view(MagazineModelView(models.Magazine, db.session, name='Журналы', category='Модели', endpoint='unique_magazine_admin'))
    admin.add_view(MyModelView(models.Author, db.session, name='Авторы', category='Модели', endpoint='unique_author_admin'))
    admin.add_view(MyModelView(models.Contact, db.session, name='Контакты', category='Модели', endpoint='unique_contact_admin'))
    admin.add_view(MyModelView(models.Event, db.session, name='События', category='Модели', endpoint='unique_event_admin'))
    admin.add_view(NewsModelView(models.News, db.session, name='Новости', category='Модели', endpoint='unique_news_admin'))
    admin.add_view(MyModelView(models.Publications, db.session, name='Публикации', category='Модели', endpoint='unique_publications_admin'))
    admin.add_view(MyModelView(models.Project, db.session, name='Проекты', category='Модели', endpoint='unique_project_admin'))
    admin.add_view(MyModelView(models.Organisation, db.session, name='Организации', category='Модели', endpoint='unique_organisation_admin'))
    # admin.add_view(MyFileAdmin())
    

def create_app(config_path = 'app.config.Config', mail = mail):
    app = Flask(__name__)
    app.config.from_object(config_path)
    #app.config['DEBUG'] = True

    basic_auth.init_app(app)

    handler = logging.StreamHandler()
    handler.setLevel(app.config.get("LOG_LEVEL", logging.INFO))
    formatter = logging.Formatter(app.config.get("LOG_FORMAT"))
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Инициализация расширений
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    admin = Admin(name='Admin Panel', template_mode='bootstrap3', index_view = MyAdminIndexView())
    #admin = Admin(name='Admin Panel', template_mode='bootstrap3')
    admin.init_app(app)

    # cache.init_app(app)

    # Регистрация представлений Flask-Admin
    register_admin_views(admin, db)  # Вызов функции

    # Регистрация Blueprint
    from .routes import main
    app.register_blueprint(main)

    #CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
    # CORS(app, supports_credentials=True, origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost",  "http://localhost:5000", "http://localhost:8080", "http://94.158.219.154:3000",
    # "http://frontend:80", "http://kapitanlevan.com:3000"])


    CORS(app,
        origins=app.config["CORS_ORIGINS"],
        methods=app.config["CORS_METHODS"],
        allow_headers=app.config["CORS_ALLOW_HEADERS"],
        expose_headers=app.config["CORS_EXPOSE_HEADERS"],
        supports_credentials=app.config["CORS_SUPPORTS_CREDENTIALS"],
        max_age=app.config["CORS_MAX_AGE"]
    )

    with app.app_context():
        db.create_all()

    print("CREATE APP")
    return app