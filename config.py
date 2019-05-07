import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = TRUE
    DATABASE_URI = os.environ['DATABASE_URL']


