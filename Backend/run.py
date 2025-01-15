from app.__init__ import create_app
from seed_db import seed_events 
from seed_projects import seed_projects
from seed_news import seed_news

app = create_app()

if __name__ == '__main__':
    seed_events()
    seed_projects()
    seed_news()
    app.run(host='0.0.0.0', port=5000)
