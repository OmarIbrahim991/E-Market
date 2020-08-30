from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path


db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    Migrate(app, db, directory=path.join("src/models", "migrations"))
