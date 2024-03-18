import getpass
import unittest

from flask.cli import FlaskGroup

from . import wsgi


cli = FlaskGroup(wsgi)
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