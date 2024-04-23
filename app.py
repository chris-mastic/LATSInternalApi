#!/usr/local/bin/python3.10
from src import create_app, db
from flask_migrate import Migrate

application = create_app()
migrate = Migrate(application, db)