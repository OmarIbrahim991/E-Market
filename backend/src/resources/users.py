from flask import request, abort
from flask_restful import Resource
from auth import requires_auth
from models.users import User


class Users(Resource):
    def get(self):
        payload = requires_auth(request.headers.get("Authorization"))

        try:
            user = User.query.filter_by(user_id=payload["sub"]).one_or_none()
        except Exception:
            abort(500)
        if user:
            return {"success": True, "user": user.format()}

        try:
            user = User(user_id=payload["sub"])
            user.insert()
        except Exception:
            abort(422)
        return {"success": True, "user": user.format()}

    def patch(self):
        payload = requires_auth(request.headers.get("Authorization"))

        try:
            user = User.query.filter_by(user_id=payload["sub"]).one_or_none()
        except Exception:
            abort(500)

        try:
            data = request.get_json()
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.completed = all((user.first_name, user.last_name))
            user.update()
        except Exception:
            abort(422)

        return {"success": True, "user": user.format()}
