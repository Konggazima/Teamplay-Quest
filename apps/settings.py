"""
settings.py

Configuration for Flask app

"""


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "hack-secret-key"
    debug = False


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "hiphopgn19@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///teamplayquest?instance=gogoxam88:lluos-testblog'
    migration_directory = 'migrations'

