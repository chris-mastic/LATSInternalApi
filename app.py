activate_this = 'venv/bin/activate'
with open(activate_this) as file_:
    exec(file_.read(), {'__file__': activate_this})


from src import create_app
application = create_app()