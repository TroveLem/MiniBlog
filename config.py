import os

# WTF_CSRF_ENABLED = True
SECRET_KEY = 'os.urandom(0)'


class BaseConfig(object):
    DEBUG = False  # switch to True if only class config
    SECRET_KEY = 'os.urandom(24)'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# export DATABASE_URL="postgresql://localhost/trove"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
