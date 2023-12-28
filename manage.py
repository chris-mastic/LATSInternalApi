import getpass
import unittest

from flask.cli import FlaskGroup

from src import app


cli = FlaskGroup(app)
print("just after creating Flask App")

@cli.command("test")
def test():
    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


if __name__ == "__main__":
    cli() 