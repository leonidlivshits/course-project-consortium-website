# Backend/seed_projects.py
from app import create_app
from app.models import db, Project

app = create_app()

def seed_projects():
    with app.app_context():
        # Удаляем все существующие проекты (опционально)
        db.session.query(Project).delete()

        # Добавляем тестовые проекты
        project1 = Project(
            title="Проект 1",
            authors="Иванов И.И., Петров П.П.",
            publication_date="2024-01-01",
            description="Описание проекта 1",
            content="Основной текст проекта 1",
            materials="https://example.com/materials1"
        )
        project2 = Project(
            title="Проект 2",
            authors="Сидоров С.С.",
            publication_date="2023-06-01",
            description="Описание проекта 2",
            content="Основной текст проекта 2",
            materials="https://example.com/materials2"
        )

        db.session.add(project1)
        db.session.add(project2)
        db.session.commit()
        print("Тестовые проекты успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_projects()