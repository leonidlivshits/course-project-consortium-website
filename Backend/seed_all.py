from datetime import datetime
from app.models import db, Author, News, Magazine, Publications, Event, Organisation, Project
from app.models import news_authors, publication_authors, project_authors

def seed_all(app):
    with app.app_context():
        # Очистка всех таблиц
        db.session.query(news_authors).delete()
        db.session.query(publication_authors).delete()
        db.session.query(project_authors).delete()
        db.session.query(News).delete()
        db.session.query(Publications).delete()
        db.session.query(Magazine).delete()
        db.session.query(Author).delete()
        db.session.query(Event).delete()
        db.session.query(Organisation).delete()
        db.session.query(Project).delete()
        db.session.commit()

        # Тестовые данные для авторов
        authors_data = [
            {"first_name": "Иван", "last_name": "Иванов", "middle_name": "Иванович"},
            {"first_name": "Петр", "last_name": "Петров", "middle_name": "Петрович"},
            {"first_name": "Сергей", "last_name": "Сидоров", "middle_name": None}
        ]

        # Создание авторов
        authors = []
        for author_data in authors_data:
            author = Author(**author_data)
            db.session.add(author)
            authors.append(author)
        db.session.commit()

        # Тестовые данные для журналов
        magazines_data = [
            {"name": "Журнал 1"},
            {"name": "Журнал 2"},
            {"name": "Журнал 3"}
        ]

        # Создание журналов
        magazines = []
        for magazine_data in magazines_data:
            magazine = Magazine(**magazine_data)
            db.session.add(magazine)
            magazines.append(magazine)
        db.session.commit()

        # Тестовые данные для новостей
        news_data = [
            {
                "title": "Новость с изображением",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "description": "Описание новости с изображением",
                "content": "Основной текст новости с изображением",
                "materials": "kitchen.jpg",
                "magazine_id": magazines[0].id,
                "author_ids": [authors[0].id, authors[1].id]
            },
            {
                "title": "Новость с аудио 1",
                "publication_date": datetime(2005, 7, 14, 12, 30),
                "description": "Описание новости с аудио 1",
                "content": "Основной текст новости с аудио 1",
                "materials": "loqiemean-как-у-людеи.mp3",
                "magazine_id": magazines[0].id,
                "author_ids": [authors[2].id]
            },
            {
                "title": "Новость с аудио 2",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "description": "Описание новости с аудио 2",
                "content": "Основной текст новости с аудио 2",
                "materials": "loqiemean-потом.mp3",
                "magazine_id": magazines[0].id,
                "author_ids": [authors[0].id]
            }
        ]

        # Создание новостей
        for news_item in news_data:
            news = News(
                title=news_item["title"],
                publication_date=news_item["publication_date"],
                description=news_item["description"],
                content=news_item["content"],
                materials=news_item["materials"],
                magazine_id=news_item["magazine_id"]
            )
            for author_id in news_item["author_ids"]:
                author = Author.query.get(author_id)
                news.authors.append(author)
            db.session.add(news)
        db.session.commit()

        # Тестовые данные для публикаций
        publications_data = [
            {
                "title": "Публикация 1",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "magazine_id": magazines[0].id,
                "annotation": "Аннотация публикации 1",
                "author_ids": [authors[0].id, authors[1].id]
            },
            {
                "title": "Публикация 2",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "magazine_id": magazines[0].id,
                "annotation": "Аннотация публикации 2",
                "author_ids": [authors[2].id]
            }
        ]

        # Создание публикаций
        for publication_item in publications_data:
            publication = Publications(
                title=publication_item["title"],
                publication_date=publication_item["publication_date"],
                magazine_id=publication_item["magazine_id"],
                annotation=publication_item["annotation"]
            )
            for author_id in publication_item["author_ids"]:
                author = Author.query.get(author_id)
                publication.authors.append(author)
            db.session.add(publication)
        db.session.commit()

        # Тестовые данные для событий
        events_data = [
            {
                "title": "Конференция",
                "date": "15 января 2025",
                "time": "15:00",
                "location": "Москва, Россия",
                "description": "Присоединяйтесь к нашей ежегодной конференции по кардиогенетике!"
            },
            {
                "title": "Семинар",
                "date": "22 февраля 2025",
                "time": "15:00",
                "location": "Санкт-Петербург, Россия",
                "description": "Узнайте о последних методах в кардиогенетике на нашем семинаре."
            },
            {
                "title": "Вебинар",
                "date": "10 марта 2025",
                "time": "15:00",
                "location": "Онлайн",
                "description": "Не пропустите наш вебинар о генетических тестах!"
            }
        ]

        # Создание событий
        for event_data in events_data:
            event = Event(**event_data)
            db.session.add(event)
        db.session.commit()

        # Тестовые данные для организаций
        organisations_data = [
            {
                "image": "/hse_logo.png",
                "link": "https://habr.com/ru/articles/321256/"
            },
            {
                "image": "/hse_logo.png",
                "link": "https://t.me/vyshkochka"
            }
        ]

        # Создание организаций
        for org_data in organisations_data:
            org = Organisation(**org_data)
            db.session.add(org)
        db.session.commit()

        # Тестовые данные для проектов
        projects_data = [
            {
                "title": "Проект с изображением",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "description": "Описание проекта с изображением",
                "content": "Основной текст проекта с изображением",
                "materials": "kitchen.jpg",
                "author_ids": [authors[0].id, authors[1].id]
            },
            {
                "title": "Проект с аудио 1",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "description": "Описание проекта с аудио 1",
                "content": "Основной текст проекта с аудио 1",
                "materials": "loqiemean-как-у-людеи.mp3",
                "author_ids": [authors[2].id]
            },
            {
                "title": "Проект с аудио 2",
                "publication_date": datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
                "description": "Описание проекта с аудио 2",
                "content": "Основной текст проекта с аудио 2",
                "materials": "loqiemean-потом.mp3",
                "author_ids": [authors[0].id]
            }
        ]

        # Создание проектов
        for project_item in projects_data:
            project = Project(
                title=project_item["title"],
                publication_date=project_item["publication_date"],
                description=project_item["description"],
                content=project_item["content"],
                materials=project_item["materials"]
            )
            for author_id in project_item["author_ids"]:
                author = Author.query.get(author_id)
                project.authors.append(author)
            db.session.add(project)
        db.session.commit()

        print("Все тестовые данные успешно добавлены в базу данных!")