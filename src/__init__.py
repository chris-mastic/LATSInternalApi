
import sys
from dotenv import load_dotenv
from flask import Flask
from flask_session import Session
import os

from config import Config as config


""" Function responsible for setting up the Flask application.
    It initializes the app, configures extensions, registers
    the two blueprints and returns the created application object
    which can be accessed via current_app
"""


def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config['DEBUG'] = config.DEBUG
    app.config['DEVELOPMENT'] = config.DEVELOPMENT
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['FLASK_APP'] = config.FLASK_APP
    app.config['MONGO_URI'] = config.MONGO_URI
    app.config['MONGO_DBNAME'] = config.MONGO_DBNAME
    app.config['LTC_API_URL_TEST'] = config.LTC_API_URL_TEST
    app.config['LTC_API_URL_PROD'] = config.LTC_API_URL_PROD
    app.config['MYSQL_USER'] = config.MYSQL_USER
    app.config['MYSQL_HOST'] = config.MYSQL_HOST
    app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
    app.config['MYSQL_DATABASE'] = config.MYSQL_DATABASE
    Session(app)

  
   # If referring to a db, this code is preferrable
    # in models.py, i.e., do something like this: db = SQLAlchemy()
    # from yourapplication.model import db
    # db.init_app(app)

    from src.authentication.views import authentication_bp
    from src.change_order.views import change_order_bp

    app.register_blueprint(authentication_bp)
    app.register_blueprint(change_order_bp)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    # return an instance of the Flask class
    # it encapsulates the entire web application,
    # including routes, views, etc

    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
