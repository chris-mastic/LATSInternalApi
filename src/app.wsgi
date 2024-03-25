import sys
#

sys.path.insert(0, '/var/www/LATSInternalApi')

activate_this = '/var/www/LATSInternalApi/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from src import create_app

application = create_app()



