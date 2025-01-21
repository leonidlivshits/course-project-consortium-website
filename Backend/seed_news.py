# # Backend/seed_projects.py
# from app import create_app
# from app.models import db, News

# app = create_app()

# def seed_news():
#     with app.app_context():
#         # Удаляем все существующие проекты (опционально)
#         db.session.query(News).delete()

#         # Добавляем тестовые проекты
#         news1 = News(
#             title="Новость",
#             authors="Иванов И.И., Петров П.П.",
#             publication_date="2024-01-01",
#             description="Описание проекта 1",
#             content="Основной текст проекта 1",
#             materials="https://example.com/materials1"
#         )
#         news2 = News(
#             title="Новость 2",
#             authors="Сидоров С.С.",
#             publication_date="2023-06-01",
#             description="Описание проекта 2",
#             magazine = "Саня гей",
#             content="Основной текст проекта 2",
#             materials="https://example.com/materials2"
#         )

#         db.session.add(news1)
#         db.session.add(news2)
#         db.session.commit()
#         print("Тестовые новости успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_news()


# Backend/seed_news.py
from app import create_app
from app.models import db, News, Author, Magazine, news_authors

app = create_app()

def seed_news():
    with app.app_context():
        # Очистка таблиц News и news_authors
        db.session.query(news_authors).delete()  # Очищаем промежуточную таблицу
        db.session.query(News).delete()  # Очищаем таблицу News
        db.session.commit()

        # Получаем существующих авторов и журналы
        author1 = Author.query.filter_by(first_name="Иван", last_name="Иванов").first()
        author2 = Author.query.filter_by(first_name="Петр", last_name="Петров").first()
        author3 = Author.query.filter_by(first_name="Сергей", last_name="Сидоров").first()

        magazine = Magazine.query.filter_by(name="Журнал 1").first()

        if not author1 or not author2 or not author3 or not magazine:
            print("Ошибка: Авторы или журналы не найдены. Запустите скрипты seed_authors.py и seed_magazines.py.")
            return

        # Добавляем тестовые новости
        news1 = News(
            title="Новость 1",
            publication_date="2024-01-01",
            description="Описание новости 1",
            content="Основной текст новости 1",
            materials="https://example.com/materials1",
            magazine_id=magazine.id
        )
        news1.authors.append(author1)
        news1.authors.append(author2)

        news2 = News(
            title="Новость 2",
            publication_date="2023-06-01",
            description="Описание новости 2",
            content="Основной текст новости 2",
            materials="https://example.com/materials2",
            magazine_id=magazine.id
        )
        news2.authors.append(author3)

        db.session.add(news1)
        db.session.add(news2)
        db.session.commit()
        print("Тестовые новости успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_news()