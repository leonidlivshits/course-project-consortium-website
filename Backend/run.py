from app import create_app
from seed_db import seed_events 
from seed_projects import seed_projects
from seed_news import seed_news
from seed_publications import seed_publications
from seed_organisations import seed_organisations
from seed_authors import seed_authors
from seed_magazines import seed_magazines

app = create_app()

def seed_all():
    """Функция для запуска всех скриптов заполнения базы данных."""
    with app.app_context():
        seed_authors(app)
        seed_magazines(app)
        seed_events(app)
        seed_projects(app)
        seed_news(app)
        seed_publications(app)
        seed_organisations(app)
        print("Все данные успешно добавлены в базу данных!")

if __name__ == '__main__':
    import sys
    if '--seed' in sys.argv:
        seed_all()
    app.run(host='0.0.0.0', port=5000)