from werkzeug.exceptions import HTTPException


class AuthError(HTTPException):
    def __init__(self, error, status_code):
        self.message = error
        self.status_code = status_code
        self.response = {
            "success": False,
            "status": self.status_code,
            "message": self.message
        }, self.status_code
