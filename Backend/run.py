#from __init__ import create_app, mail
#from Backend import create_app, mail
#from app import create_app
from app.__init__ import create_app
from seed_db import seed_events 
from seed_projects import seed_projects
app = create_app()

if __name__ == '__main__':
    seed_events()
    seed_projects()
    app.run(host='0.0.0.0', port=5000)
