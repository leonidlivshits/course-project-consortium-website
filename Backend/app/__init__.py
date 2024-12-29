# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')

#     db.init_app(app)

#     with app.app_context():
#         db.create_all()

#     from .routes import main
#     app.register_blueprint(main)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import flask_cors as CORS
# import flask_mail as Mail
# from app.config import Config

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail
# from flask_cors import CORS
# from app.config import Config

# db = SQLAlchemy()
# #mail = Mail.Mail()
# mail = Mail()
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     mail.init_app(app)

#     with app.app_context():
#         #from .app import routes
#         from app import routes
#         db.create_all()
#         print("Database initialized.")

#     CORS.CORS(app)

#     return app




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from .config import Config

from flask_cors import CORS

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['DEBUG'] = True
    db.init_app(app)
    mail.init_app(app)
    CORS(app)
    
    #CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
    # Регистрация Blueprint
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
