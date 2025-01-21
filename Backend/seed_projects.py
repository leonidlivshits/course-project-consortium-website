# # Backend/seed_projects.py
# from app import create_app
# from app.models import db, Project

# app = create_app()

# def seed_projects():
#     with app.app_context():
#         # Удаляем все существующие проекты (опционально)
#         db.session.query(Project).delete()

#         # Добавляем тестовые проекты
#         project1 = Project(
#             title="Проект 1",
#             authors="Иванов И.И., Петров П.П.",
#             publication_date="2024-01-01",
#             description="Описание проекта 1",
#             content="Основной текст проекта 1",
#             materials="https://example.com/materials1"
#         )
#         project2 = Project(
#             title="Проект 2",
#             authors="Сидоров С.С.",
#             publication_date="2023-06-01",
#             description="Описание проекта 2",
#             content="Основной текст проекта 2",
#             materials="https://example.com/materials2"
#         )

#         db.session.add(project1)
#         db.session.add(project2)
#         db.session.commit()
#         print("Тестовые проекты успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_projects()

# Backend/seed_projects.py
from app import create_app
from app.models import db, Project, Author, project_authors

app = create_app()

def seed_projects():
    with app.app_context():
        # Очистка таблиц Project и project_authors
        db.session.query(project_authors).delete()  # Очищаем промежуточную таблицу
        db.session.query(Project).delete()  # Очищаем таблицу Project
        db.session.commit()

        # Получаем существующих авторов
        author1 = Author.query.filter_by(first_name="Иван", last_name="Иванов").first()
        author2 = Author.query.filter_by(first_name="Петр", last_name="Петров").first()
        author3 = Author.query.filter_by(first_name="Сергей", last_name="Сидоров").first()

        if not author1 or not author2 or not author3:
            print("Ошибка: Авторы не найдены. Запустите скрипт seed_authors.py.")
            return

        # Добавляем тестовые проекты
        project1 = Project(
            title="Проект 1",
            publication_date="2024-01-01",
            description="Описание проекта 1",
            content="Основной текст проекта 1",
            materials="https://example.com/materials1"
        )
        project1.authors.append(author1)
        project1.authors.append(author2)

        project2 = Project(
            title="Проект 2",
            publication_date="2023-06-01",
            description="Описание проекта 2",
            content="Основной текст проекта 2",
            materials="https://example.com/materials2"
        )
        project2.authors.append(author3)

        db.session.add(project1)
        db.session.add(project2)
        db.session.commit()
        print("Тестовые проекты успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_projects()