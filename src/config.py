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
    ORACLE_CONNECTSTRING = config.get("ORACLE_CONNECTSTRING")
    ORACLE_PASSWORD = config.get("ORACLE_PASSWORD")
    ORACLE_USERNAME = config.get("ORACLE_USERNAME")
    MYSQL_HOST = config.get("MYSQL_HOST")
    MYSQL_USER = config.get("MYSQL_USER")
    MYSQL_PASSWORD = config.get("MYSQL_PASSWORD")
    MYSQL_DATABASE = config.get("MYSQL_DATABASE")
    LTC_API_URL_TEST = config.get("LTC_API_URL_TEST")
    LTC_API_URL_PROD = config.get("LTC_API_URL_PROD")
    MONGO_URI = config.get("MONGO_URI")
    MONGO_DBNAME = config.get("MONGO_DBNAME")
    EXPO_URL = config.get("EXPO_URL")
    #DEBUG = False #Prod
    DEBUG = True #Development
    DEVELOPMENT = True
    #SESSION_TYPE = config.get("SESSION_TYPE") # use with sessionid
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    
