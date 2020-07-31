import os
from flask import Flask
from todo.database import init_db
from todo import models

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    config = {
        "development": "todo.config.DevelopmentConfig",
        #"testing": "todo.config.TestingConfig",
        "default": "todo.config.DevelopmentConfig"
    }

    # 環境変数を利用して読み込む設定ファイルを決定
    config_name = os.getenv('FLASK_ENV', 'default')

    # 設定はオブジェクトとして読み込む
    app.config.from_object(config[config_name])

    # センシティブな設定はインスタンスフォルダ内の設定で上書きする
    app.config.from_pyfile('config.cfg', silent=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.cfg', silent=True)
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
        return f'hello'

    init_db(app)

    return app
