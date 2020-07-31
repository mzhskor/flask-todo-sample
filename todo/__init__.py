import os
from flask import Flask
from todo.database import init_db
from todo import models

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{host}/mydb'.format(**{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'root'),
            'host': os.getenv('DB_HOST', 'db'),
        }),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    print(app.instance_path)

    @app.route('/hello')
    def hello():
        return f'hello {app.instance_path}'

    init_db(app)

    return app
