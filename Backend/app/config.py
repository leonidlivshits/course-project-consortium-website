# class Config:
#     #SQLALCHEMY_DATABASE_URI = 'postgresql://cardio_user:CardioGenHSE@localhost/cardiogenetics_db'
#     SQLALCHEMY_DATABASE_URI = 'postgresql://cardio_user:CardioGenHSE@db:5432/cardiogenetics_db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
#     MAIL_PORT = 2525
#     MAIL_USERNAME = '4fe42efc490081'
#     MAIL_PASSWORD = '6105673a02dbe9'
#     MAIL_USE_TLS = True
#     MAIL_USE_SSL = False

class Config:
    #SQLALCHEMY_DATABASE_URI = 'postgresql://cardio_user:CardioGenHSE@db:5432/cardiogenetics_db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://cardio_user:CardioGenHSE@localhost:5432/cardiogenetics_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '4fe42efc490081'
    MAIL_PASSWORD = '6105673a02dbe9'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False