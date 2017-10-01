from flask import Flask
from configs import app_configs
from flask_pymongo import PyMongo

from apps import main,api

def create_app(config_name = 'develop' ):
    app = Flask(__name__)
    app.config.from_object( app_configs[ config_name ] )

    # Blueprint の登録.
    app.register_blueprint( main.app )
    app.register_blueprint( api.app )

    app.mongo = PyMongo(app)

    return app

def create_app_unittest():
    app = create_app( 'testing' )
    return app