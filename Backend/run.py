# from app.__init__ import create_app
# from seed_db import seed_events 
# from seed_projects import seed_projects
# from seed_news import seed_news
# from seed_publications import seed_publications
# from seed_organisations import seed_organisations
# from seed_authors import seed_authors
# from seed_magazines import seed_magazines
# app = create_app()

# if __name__ == '__main__':
#     seed_authors()
#     seed_magazines()
#     seed_events()
#     seed_projects()
#     seed_news()
#     seed_publications()
#     seed_organisations()

#     app.run(host='0.0.0.0', port=5000)
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
        seed_authors()
        seed_magazines()
        seed_events()
        seed_projects()
        seed_news()
        seed_publications()
        seed_organisations()
        print("Все данные успешно добавлены в базу данных!")

if __name__ == '__main__':
    # Запуск всех скриптов для заполнения базы данных
    seed_all()
    
    # Запуск Flask-приложения
    app.run(host='0.0.0.0', port=5000)