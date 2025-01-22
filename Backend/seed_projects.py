

# # Backend/seed_projects.py
# from app import create_app
# from app.models import db, Project, Author, project_authors

# app = create_app()

# def seed_projects():
#     with app.app_context():
#         # Очистка таблиц Project и project_authors
#         db.session.query(project_authors).delete()  # Очищаем промежуточную таблицу
#         db.session.query(Project).delete()  # Очищаем таблицу Project
#         db.session.commit()

#         # Получаем существующих авторов
#         author1 = Author.query.filter_by(first_name="Иван", last_name="Иванов").first()
#         author2 = Author.query.filter_by(first_name="Петр", last_name="Петров").first()
#         author3 = Author.query.filter_by(first_name="Сергей", last_name="Сидоров").first()

#         if not author1 or not author2 or not author3:
#             print("Ошибка: Авторы не найдены. Запустите скрипт seed_authors.py.")
#             return

#         # Добавляем тестовые проекты
#         project1 = Project(
#             title="Проект 1",
#             publication_date="2024-01-01",
#             description="Описание проекта 1",
#             content="Основной текст проекта 1",
#             materials="https://example.com/materials1"
#         )
#         project1.authors.append(author1)
#         project1.authors.append(author2)

#         project2 = Project(
#             title="Проект 2",
#             publication_date="2023-06-01",
#             description="Описание проекта 2",
#             content="Основной текст проекта 2",
#             materials="https://example.com/materials2"
#         )
#         project2.authors.append(author3)

#         db.session.add(project1)
#         db.session.add(project2)
#         db.session.commit()
#         print("Тестовые проекты успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_projects()


# import os
# from app import create_app
# from app.models import db, Project, Author, project_authors

# app = create_app()

# def seed_projects():
#     with app.app_context():
#         # Очистка таблиц Project и project_authors
#         db.session.query(project_authors).delete()  # Очищаем промежуточную таблицу
#         db.session.query(Project).delete()  # Очищаем таблицу Project
#         db.session.commit()

#         # Получаем существующих авторов
#         author1 = Author.query.filter_by(first_name="Иван", last_name="Иванов").first()
#         author2 = Author.query.filter_by(first_name="Петр", last_name="Петров").first()
#         author3 = Author.query.filter_by(first_name="Сергей", last_name="Сидоров").first()

#         if not author1 or not author2 or not author3:
#             print("Ошибка: Авторы не найдены. Запустите скрипт seed_authors.py.")
#             return

#         # Путь к папке uploads
#         UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
#         os.makedirs(UPLOADS_DIR, exist_ok=True)

#         # Копируем тестовые файлы в папку uploads
#         test_files = {
#             "kitchen.jpg": "kitchen.jpg",
#             "loqiemean-как-у-людеи.mp3": "loqiemean-как-у-людеи.mp3",
#             "loqiemean-потом.mp3": "loqiemean-потом.mp3",
#         }

#         for src, dest in test_files.items():
#             src_path = os.path.join("path_to_your_test_files", src)  # Укажите путь к тестовым файлам
#             dest_path = os.path.join(UPLOADS_DIR, dest)
#             if os.path.exists(src_path):
#                 with open(src_path, 'rb') as src_file, open(dest_path, 'wb') as dest_file:
#                     dest_file.write(src_file.read())

#         # Добавляем тестовые проекты
#         project1 = Project(
#             title="Проект с изображением",
#             publication_date="2024-01-01",
#             description="Описание проекта с изображением",
#             content="Основной текст проекта с изображением",
#             materials="kitchen.jpg"  # Имя файла
#         )
#         project1.authors.append(author1)
#         project1.authors.append(author2)

#         project2 = Project(
#             title="Проект с аудио 1",
#             publication_date="2023-06-01",
#             description="Описание проекта с аудио 1",
#             content="Основной текст проекта с аудио 1",
#             materials="loqiemean-как-у-людеи.mp3"  # Имя файла
#         )
#         project2.authors.append(author3)

#         project3 = Project(
#             title="Проект с аудио 2",
#             publication_date="2023-12-01",
#             description="Описание проекта с аудио 2",
#             content="Основной текст проекта с аудио 2",
#             materials="loqiemean-потом.mp3"  # Имя файла
#         )
#         project3.authors.append(author1)

#         db.session.add(project1)
#         db.session.add(project2)
#         db.session.add(project3)
#         db.session.commit()
#         print("Тестовые проекты успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_projects()

import os
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

        # Путь к папке uploads
        UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
        os.makedirs(UPLOADS_DIR, exist_ok=True)

        # Проверяем, что файлы существуют в папке uploads
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

        # Добавляем тестовые проекты
        project1 = Project(
            title="Проект с изображением",
            publication_date="2024-01-01",
            description="Описание проекта с изображением",
            content="Основной текст проекта с изображением",
            materials="kitchen.jpg"  # Имя файла
        )
        project1.authors.append(author1)
        project1.authors.append(author2)

        project2 = Project(
            title="Проект с аудио 1",
            publication_date="2023-06-01",
            description="Описание проекта с аудио 1",
            content="Основной текст проекта с аудио 1",
            materials="loqiemean-как-у-людеи.mp3"  # Имя файла
        )
        project2.authors.append(author3)

        project3 = Project(
            title="Проект с аудио 2",
            publication_date="2023-12-01",
            description="Описание проекта с аудио 2",
            content="Основной текст проекта с аудио 2",
            materials="loqiemean-потом.mp3"  # Имя файла
        )
        project3.authors.append(author1)

        db.session.add(project1)
        db.session.add(project2)
        db.session.add(project3)
        db.session.commit()
        print("Тестовые проекты успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_projects()