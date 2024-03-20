from decouple import config


# DATABASE_URI = config("DATABASE_URL")
# if DATABASE_URI.startswith("postgres://"):
#     DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

# Create a Config class


class Config(object):
    """Define various class attributes. We have also created different
        child classes (as per different stages of development) tha inherit
        the Config class"""
    # Environment variables
    print("INSIDE class Config()")
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default="guess-me")
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    FLASK_DEBUG=True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False
