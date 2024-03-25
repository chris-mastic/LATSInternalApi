activate_this = 'venv/bin/activate'
exec(open(activate_this).read(), dict(__file__=activate_this))

from src import create_app

application = create_app()
