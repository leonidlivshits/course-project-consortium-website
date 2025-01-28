from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
import logging

logger = logging.getLogger(__name__)

# Флаг для отслеживания регистрации представлений
_views_registered = False

def register_admin_views(admin: Admin, db: SQLAlchemy):
    global _views_registered

    # Если представления уже зарегистрированы, пропускаем
    if _views_registered:
        return

    try:
        from .models import Magazine, Author, Contact, Event, News, Publications, Project, Organisation

        # Регистрация ModelView
        admin.add_view(ModelView(Magazine, db.session, name='Журналы', category='Модели', endpoint='unique_magazine_admin'))
        admin.add_view(ModelView(Author, db.session, name='Авторы', category='Модели', endpoint='unique_author_admin'))
        admin.add_view(ModelView(Contact, db.session, name='Контакты', category='Модели', endpoint='unique_contact_admin'))
        admin.add_view(ModelView(Event, db.session, name='События', category='Модели', endpoint='unique_event_admin'))
        admin.add_view(ModelView(News, db.session, name='Новости', category='Модели', endpoint='unique_news_admin'))
        admin.add_view(ModelView(Publications, db.session, name='Публикации', category='Модели', endpoint='unique_publications_admin'))
        admin.add_view(ModelView(Project, db.session, name='Проекты', category='Модели', endpoint='unique_project_admin'))
        admin.add_view(ModelView(Organisation, db.session, name='Организации', category='Модели', endpoint='unique_organisation_admin'))

        _views_registered = True  # Устанавливаем флаг

    except ValueError as e:
        logger.error(f"Ошибка регистрации представлений: {e}")
        raise