from datetime import datetime
from app.models import db, Publications, Author, Magazine, publication_authors

def seed_publications(app):
    with app.app_context():
        # Очистка таблиц Publications и publication_authors
        db.session.query(publication_authors).delete()
        db.session.query(Publications).delete()
        db.session.commit()

        # Получаем существующих авторов и журналы
        author1 = Author.query.filter_by(first_name="Иван", last_name="Иванов").first()
        author2 = Author.query.filter_by(first_name="Петр", last_name="Петров").first()
        author3 = Author.query.filter_by(first_name="Сергей", last_name="Сидоров").first()

        magazine = Magazine.query.filter_by(name="Журнал 1").first()

        if not author1 or not author2 or not author3 or not magazine:
            print("Ошибка: Авторы или журналы не найдены. Запустите скрипты seed_authors.py и seed_magazines.py.")
            return

        publication1 = Publications(
            title="Публикация 1",
            publication_date=datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
            magazine_id=magazine.id,
            annotation="Аннотация публикации 1"
        )
        publication1.authors.append(author1)
        publication1.authors.append(author2)

        publication2 = Publications(
            title="Публикация 2",
            publication_date=datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
            magazine_id=magazine.id,
            annotation="Аннотация публикации 2"
        )
        publication2.authors.append(author3)

        db.session.add(publication1)
        db.session.add(publication2)
        db.session.commit()
        print("Тестовые публикации успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_publications()