from app.models import db, Event

def seed_events(app):
    with app.app_context():
        db.session.query(Event).delete()

        event1 = Event(
            title="Конференция",
            date="15 января 2025",
            time="15:00",
            location="Москва, Россия",
            description="Присоединяйтесь к нашей ежегодной конференции по кардиогенетике!"
        )
        event2 = Event(
            title="Семинар",
            date="22 февраля 2025",
            time="15:00",
            location="Санкт-Петербург, Россия",
            description="Узнайте о последних методах в кардиогенетике на нашем семинаре."
        )
        event3 = Event(
            title="Вебинар",
            date="10 марта 2025",
            time="15:00",
            location="Онлайн",
            description="Не пропустите наш вебинар о генетических тестах!"
        )

        db.session.add(event1)
        db.session.add(event2)
        db.session.add(event3)
        db.session.commit()
        print("Тестовые события успешно добавлены в базу данных!")

# if __name__ == "__main__":
#     seed_events()