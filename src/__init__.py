
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os

from .config import *


""" Function responsible for setting up the Flask application.
    It initializes the app, configures extensions, registers
    the two blueprints and returns the created application object
"""


def create_app():
    load_dotenv()
    print("in the stupid factory method")
    app = Flask(__name__)

    if app.config['FLASK_ENV'] == 'development':
        app.config.from_object(DevelopmentConfig)
    elif app.config['FLASK_ENV'] == 'production':
        app.config.from_object(ProductionConfig)
    elif app.config['FLASK_ENV'] == 'Testing':
        app.config.from_object(TestingConfig)
    app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE')
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    app.config['APP_SETTINGS'] = os.getenv('APP_SETTINGS')
    app.config['FLASK_APP'] = os.getenv('FLASK_APP')
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
    Session(app)

   # Enable CORS for specific routes (e.g., /api/*)
    cors = CORS(app, resources={r"/api/*": {"origins": os.getenv('EXPO_URL')}},
                allow_headers=["Content-Type", "Authorization"],
                supports_credentials=True)

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
    print("inside if __name__")
    my_app = create_app()
    my_app.run(debug=True)
