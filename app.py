#!/usr/local/bin/python3.10
#

activate_this = '/var/www/LATSInternalApi/venv/bin/activate'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from src import create_app
application = create_app()