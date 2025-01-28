from app.models import db, Author, news_authors, publication_authors

def seed_authors(app):
    with app.app_context():
        # Очистка промежуточных таблиц перед удалением авторов
        db.session.query(news_authors).delete()
        db.session.query(publication_authors).delete() 
        db.session.commit()

        # Очистка таблицы Author
        db.session.query(Author).delete()
        db.session.commit()

        # Добавляем тестовых авторов
        author1 = Author(
            first_name="Иван",
            last_name="Иванов",
            middle_name="Иванович"
        )
        author2 = Author(
            first_name="Петр",
            last_name="Петров",
            middle_name="Петрович"
        )
        author3 = Author(
            first_name="Сергей",
            last_name="Сидоров",
            middle_name=None  # Отчество отсутствует
        )

        db.session.add(author1)
        db.session.add(author2)
        db.session.add(author3)
        db.session.commit()
        print("Тестовые авторы успешно добавлены в базу данных!")