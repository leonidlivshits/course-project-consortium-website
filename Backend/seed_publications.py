from app import create_app
from app.models import db, Publications

app = create_app()

def seed_publications():
    with app.app_context():
        db.session.query(Publications).delete()

        # Добавляем тестовые проекты
        publication1 = Publications(
            title="Новость",
            authors="Иванов И.И., Петров П.П.",
            publication_date="2024-01-01",
            magazine = "Саня гей",
            annotation="Основной текст проекта 1",
        )
        publication2 = Publications(
            title="Новость 2",
            authors="Сидоров С.С.",
            publication_date="2023-06-01",
            magazine = "Саня гей",
            annotation="Основной текст проекта 2",
        )

        db.session.add(publication1)
        db.session.add(publication2)
        db.session.commit()
        print("Тестовые публикации успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_publications()