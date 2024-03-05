
from flask import Flask
from flask_session import Session
import os
from dotenv import load_dotenv


# additional_paths = [
#     '/var/www/LATSInternalApi/src',
#     '/var/www/LATSInternalApi/src/db',
#     '/var/www/LATSInternalApi/src/services'
#         ]  
# sys.path.extend(additional_paths)


def create_app():
    load_dotenv()
    print("In create_app()")
    app = Flask(__name__)
    app.config['SESSION_TYPE']=os.getenv('SESSION_TYPE')
    app.config['SECRET_KEY']=os.getenv('FLASK_SECRET_KEY')
    app.config['DEBUG']=os.getenv('DEBUG')
    app.config['APP_SETTINGS']=os.getenv('APP_SETTINGS')
    app.config['FLASK_APP']=os.getenv('FLASK_APP')
    app.config['FLASK_DEBUG']=os.getenv('FLASK_DEBUG')
    Session(app)

    print(f"app {app}")
    print(f"app.config['SESSION_TYPE'] {app.config['SESSION_TYPE']}")
    print(f"app.config['SECRET_KEY'] {app.config['SECRET_KEY']}")
    print(f"app.config['APP_SETTINGS'] {app.config['APP_SETTINGS']}")
    print(f"app.config['FLASK_APP'] {app.config['FLASK_APP']}")
   
    from src.authentication.views import authentication_bp
    from src.change_order.views import change_order_bp


    app.register_blueprint(authentication_bp)
    app.register_blueprint(change_order_bp)

    

    return app

if __name__ == '__main__':
    print("inside if __name__")
    my_app = create_app()
    my_app.run(debug=True)


