from decouple import config

# DATABASE_URI = config("DATABASE_URL")
# if DATABASE_URI.startswith("postgres://"):
#     DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

#Create a Config class
class Config(object):
    """Define various class attributes. We have also created different
        child classes (as per different stages of development) tha inherit
        the Config class"""
    #Environment variables
    print("class Config called")
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default="guess-me")
    # SQLALCHEMY_DATABASE_URI = DATABASE_URI
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True

       


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    #BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False