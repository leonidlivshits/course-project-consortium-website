from app.models import db, Organisation

def seed_organisations(app):
    with app.app_context():
        db.session.query(Organisation).delete()

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

# if __name__ == "__main__":
#     seed_organisations()