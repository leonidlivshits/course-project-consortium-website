import logging
import os
from dotenv import load_dotenv
from datetime import timedelta

from pathlib import Path
#print(os.urandom(12).hex())
#dotenv_path = Path(__file__).resolve().parent / ".env"
# print("ROOOOOOOOT")
# print(dotenv_path)
#load_dotenv(dotenv_path=dotenv_path)
load_dotenv()

class Config:

    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    POSTGRES_USER = os.environ.get(
    'POSTGRES_USER',
    )

    POSTGRES_DB = os.environ.get(
    'POSTGRES_DB',
    )

    POSTGRES_PASSWORD = os.environ.get(
    'POSTGRES_PASSWORD',
    )

    SQLITE_DB = os.environ.get('SQLITE_DB', )

    #SQLALCHEMY_DATABASE_URI = f"sqlite:///{SQLITE_DB}"
    DB_HOST = os.environ.get('DB_HOST', 'localhost')

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:5432/{POSTGRES_DB}"
    #SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
    'SQLALCHEMY_TRACK_MODIFICATIONS',
    )
    MAIL_SERVER = os.environ.get(
    'MAIL_SERVER',
    )
    MAIL_PORT = int(os.environ.get(
    'MAIL_PORT',
    ))
    MAIL_USERNAME = os.environ.get(
    'MAIL_USERNAME',
    )
    MAIL_PASSWORD = os.environ.get(
    'MAIL_PASSWORD',
    )
    MAIL_USE_TLS = os.environ.get(
    'MAIL_USE_TLS',
    ).lower() == "true"
    MAIL_USE_SSL = os.environ.get(
    'MAIL_USE_SSL',
    ).lower() == "true"
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
    )
    MAIL_DEFAULT_SENDER = ('No Reply', 'noreply@example.com')


    BASIC_AUTH_USERNAME=os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD=os.environ.get('BASIC_AUTH_PASSWORD')
  
    #BASIC_AUTH_FORCE = True

    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 3600

    CORS_ORIGINS = ["http://127.0.0.1:3000", "http://62.217.181.205", "http://localhost:3000"]
    #CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
    CORS_METHODS = os.environ.get('CORS_METHODS', 'GET,POST,PUT,DELETE,OPTIONS').split(',')
    CORS_ALLOW_HEADERS = os.environ.get('CORS_ALLOW_HEADERS', 'Content-Type,Authorization').split(',')
    CORS_EXPOSE_HEADERS = os.environ.get('CORS_EXPOSE_HEADERS', 'Content-Type').split(',')
    CORS_SUPPORTS_CREDENTIALS = os.environ.get('CORS_SUPPORTS_CREDENTIALS', 'False').lower() == 'true'
    CORS_MAX_AGE = int(os.environ.get('CORS_MAX_AGE', '600'))

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'sqlite:///:memory:'
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'password'
    TESTING = True
    # CORS_ORIGINS = ['http://localhost:3000']
    # CORS_METHODS = ['GET', 'POST']
    # CORS_SUPPORTS_CREDENTIALS = False