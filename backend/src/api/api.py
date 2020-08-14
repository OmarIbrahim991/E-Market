from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from models import setup_db, User

def create_app(test_config=None):

    app = Flask(__name__)

    if test_config is None:
        app.config.from_object("api.config")
    else:
        app.config.from_mapping(test_config)

    CORS(app)
    api = Api(app)
    setup_db(app)
    
    class Hello(Resource):
        def get(self):
            return {"success": True, "message": "Hello, World!"}

    api.add_resource(Hello, "/")

    return app
