from os import urandom, environ

SECRET_KEY = urandom(32)
SQLALCHEMY_DATABASE_URI = environ.get("DATABASE")
SQLALCHEMY_TRACK_MODIFICATIONS = False
