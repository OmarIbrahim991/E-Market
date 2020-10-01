def error_message(status, code, description):
    return {
        "success": False,
        "status": status,
        "message": {
            "code": code,
            "description": description
        }
    }


errors = {
    "BadRequest": error_message(400, "bad_request", "Bad request."),
    "Unauthorized": error_message(401, "unauthorized", "Not authorized."),
    "Forbidden": error_message(403, "forbidden", "Forbidden."),
    "NotFound": error_message(404, "not_found", "Resource is not found."),
    "UnprocessableEntity": error_message(422, "unprocessable", "Unprocessable."),
    "InternalServerError": error_message(500, "server_error", "Server error.")
}
