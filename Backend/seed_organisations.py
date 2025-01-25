# # Backend/seed_projects.py
# from app import create_app
# from app.models import db, Organisation

# app = create_app()

# def seed_organisations():
#     with app.app_context():
#         # Удаляем все существующие проекты (опционально)
#         db.session.query(Organisation).delete()

#         # Добавляем тестовые проекты
#         orgs1 = Organisation(
#             image = "/hse_logo.png",
#             link="https://habr.com/ru/articles/321256/"
#         )
#         orgs2 = Organisation(
#             image = "/hse_logo.png",
#             link="https://t.me/vyshkochka"
#         )

#         db.session.add(orgs1)
#         db.session.add(orgs2)
#         db.session.commit()
#         print("Тестовые организации успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_organisations()

from app import create_app
from app.models import db, Organisation

def seed_organisations():
    app = create_app()
    with app.app_context():
        # Удаляем все существующие организации (опционально)
        db.session.query(Organisation).delete()

        # Добавляем тестовые организации
        orgs1 = Organisation(
            image="/hse_logo.png",
            link="https://habr.com/ru/articles/321256/"
        )
        orgs2 = Organisation(
            image="/hse_logo.png",
            link="https://t.me/vyshkochka"
        )

        db.session.add(orgs1)
        db.session.add(orgs2)
        db.session.commit()
        print("Тестовые организации успешно добавлены в базу данных!")

if __name__ == "__main__":
    seed_organisations()