# Backend/seed_projects.py
from app import create_app
from app.models import db, News

app = create_app()

def seed_news():
    with app.app_context():
        # Удаляем все существующие проекты (опционально)
        db.session.query(News).delete()

        # Добавляем тестовые проекты
        news1 = News(
            title="Новость",
            authors="Иванов И.И., Петров П.П.",
            publication_date="2024-01-01",
            description="Описание проекта 1",
            content="Основной текст проекта 1",
            materials="https://example.com/materials1"
        )
        news2 = News(
            title="Новость 2",
            authors="Сидоров С.С.",
            publication_date="2023-06-01",
            description="Описание проекта 2",
            magazine = "Саня гей",
            content="Основной текст проекта 2",
            materials="https://example.com/materials2"
        )

        db.session.add(news1)
        db.session.add(news2)
        db.session.commit()
        print("Тестовые новости успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_news()