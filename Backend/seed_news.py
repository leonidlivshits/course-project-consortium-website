import os
from datetime import datetime
from app.models import db, News, Author, Magazine, news_authors

def seed_news(app):
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

        # Путь к папке uploads
        UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        test_files = {
            "kitchen.jpg": "kitchen.jpg",
            "loqiemean-как-у-людеи.mp3": "loqiemean-как-у-людеи.mp3",
            "loqiemean-потом.mp3": "loqiemean-потом.mp3",
        }

        for filename in test_files.values():
            file_path = os.path.join(UPLOADS_DIR, filename)
            if not os.path.exists(file_path):
                print(f"Файл {filename} не найден в папке uploads. Пропускаем.")
            else:
                print(f"Файл {filename} найден в папке uploads.")

        news1 = News(
            title="Новость с изображением",
            publication_date=datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
            description="Описание новости с изображением",
            content="Основной текст новости с изображением",
            materials="kitchen.jpg",  # Имя файла
            magazine_id=magazine.id
        )
        news1.authors.append(author1)
        news1.authors.append(author2)

        news2 = News(
            title="Новость с аудио 1",
            #publication_date=datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
            publication_date=datetime.datetime(2005, 7, 14, 12, 30),
            description="Описание новости с аудио 1",
            content="Основной текст новости с аудио 1",
            materials="loqiemean-как-у-людеи.mp3",  # Имя файла
            magazine_id=magazine.id
        )
        news2.authors.append(author3)

        news3 = News(
            title="Новость с аудио 2",
            publication_date=datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"),
            description="Описание новости с аудио 2",
            content="Основной текст новости с аудио 2",
            materials="loqiemean-потом.mp3",  # Имя файла
            magazine_id=magazine.id
        )
        news3.authors.append(author1)

        db.session.add(news1)
        db.session.add(news2)
        db.session.add(news3)
        db.session.commit()
        print("Тестовые новости успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_news()