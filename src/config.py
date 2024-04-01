from decouple import config
import json
import os

with open('config.json') as config_file:
        config = json.load(config_file)
    

class Config:
    """Define various class attributes."""
    CSRF_ENABLED = True
    SECRET_KEY = config.get("SECRET_KEY")
    FLASK_APP =config.get("FLASK_APP")
    PYTHON_CONNECTSTRING = config.get("PYTHON_CONNECTSTRING")
    PYTHON_PASSWORD = config.get("PYTHON_PASSWORD")
    PYTHON_USERNAME = config.get("PYTHON_USERNAME")
    LTC_API_URL_TEST = config.get("LTC_API_URL_TEST")
    LTC_API_URL_PROD = config.get("LTC_API_URL_PROD")
    MONGO_URI = config.get("MONGO_URI")
    MONGO_DBNAME = config.get("MONGO_DBNAME")
    EXPO_URL = config.get("EXPO_URL")
    #DEBUG = False #Prod
    DEBUG = True #Development
    DEVELOPMENT = True
    #SESSION_TYPE = config.get("SESSION_TYPE") # use with sessionid
    
