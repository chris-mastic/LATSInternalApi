import os
from flask_testing import TestCase
from . import wsgi


class BaseTestCase(TestCase):
    def create_app(self):
        wsgi.config.from_object("config.TestingConfig")
        return wsgi
    def setUp(self): pass
    
    def tearDown(self): pass