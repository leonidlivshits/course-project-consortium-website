import os
from dotenv import load_dotenv

from pathlib import Path
#print(os.urandom(12).hex())
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Config:
    
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

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
    #SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"
    #SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@host.docker.internal:5432/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
    'SQLALCHEMY_TRACK_MODIFICATIONS',
    )
    MAIL_SERVER = os.environ.get(
    'MAIL_SERVER',
    )
    MAIL_PORT = os.environ.get(
    'MAIL_PORT',
    )
    MAIL_USERNAME = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    )
    MAIL_PASSWORD = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    )
    MAIL_USE_TLS = os.environ.get(
    'MAIL_USE_TLS',
    )
    MAIL_USE_SSL = os.environ.get(
    'MAIL_USE_SSL',
    )
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
    )
