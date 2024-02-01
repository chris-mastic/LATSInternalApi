
from flask import Flask
from flask_session import Session
from flask_login import LoginManager, UserMixin, login_user, current_user
import config

import os


app = Flask(__name__)
app.config['SESSION_TYPE']= os.environ.get('SESSION_TYPE')
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
login_manager = LoginManager()
login_manager.init_app(app)

Session(app)
print("in __init__.py")
print(f"{os.environ.get('FLASK_SECRET_KEY')}")
print(f"{os.environ.get('SESSION_TYPE')}")
print(f"app.config['SESSION_TYPE'] {app.config['SESSION_TYPE']}")
print(f"app.config['SECRET_KEY']{app.config['SECRET_KEY']}")

from src.authentication.views import authentication_bp
from src.change_order.views import change_order_bp

app.register_blueprint(authentication_bp)
app.register_blueprint(change_order_bp)


