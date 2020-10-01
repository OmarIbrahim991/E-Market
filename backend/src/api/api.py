from flask import Flask, make_response, jsonify
from flask_restful import Api
from flask_cors import CORS
from models import setup_db
from resources import Users, Products
from .errors import errors


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object("api.config")
    else:
        app.config.from_mapping(test_config)

    CORS(app)
    api = Api(app, errors=errors)
    setup_db(app)

    api.add_resource(Users, "/users")
    api.add_resource(Products, "/products", "/products/<int:product_id>")

    @api.representation("application/json")
    def output_json(data, code, headers=None):
        resp = make_response(jsonify(data), code)
        resp.headers.extend(headers or {})
        return resp

    return app
