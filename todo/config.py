import os
import redis

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}/mydb'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'root'),
        'host': os.getenv('DB_HOST', 'db'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Flask-Session
    SESSION_TYPE = os.getenv('SESSION_TYPE', 'redis')
    SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS', 'redis://redis:6379'))

