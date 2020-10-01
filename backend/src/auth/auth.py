import json
from jose import jwt
from urllib.request import urlopen
from os import environ
from .errors import AuthError


AUTH0_DOMAIN = environ.get("AUTH0_DOMAIN")
ALGORITHMS = environ.get("ALGORITHMS").split(",")
API_AUDIENCE = environ.get("API_AUDIENCE")


def get_token_from_auth_header(auth_header):
    if not auth_header:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization header is expected."
        }, 401)

    auth_parts = auth_header.split()

    if auth_parts[0].lower() != "bearer":
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must start with 'Bearer'."
        }, 400)
    elif len(auth_parts) == 1:
        raise AuthError({
            "code": "invalid_header",
            "description": "Token not found."
        }, 400)
    elif len(auth_parts) > 2:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must be bearer token."
        }, 400)

    return auth_parts[1]


def verify_decode_jwt(token):
    try:
        jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
    except Exception:
        raise AuthError({
            "code": "server_error",
            "description": "Failed to fetch data from Auth0."
        }, 500)

    if "kid" not in unverified_header:
        raise AuthError({
            "code": "invalid_headers",
            "description": "No key provided."
        }, 400)

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
            break

    if not rsa_key:
        raise AuthError({
            "code": "invalid_key",
            "description": "Key does not exist."
        }, 401)

    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )
    except jwt.ExpiredSignatureError:
        raise AuthError({
            "code": "token_expired",
            "description": "Token expired."
        }, 401)
    except jwt.JWTClaimsError:
        raise AuthError({
            "code": "invalid_claims",
            "description": "Incorrect claims. check the audience and issuer."
        }, 401)
    except Exception:
        raise AuthError({
            "code": "invalid_header",
            "description": "Unable to parse authentication token."
        }, 400)

    return payload


def check_permissions(permission, payload):
    if not permission:
        return True

    if "permission" not in payload:
        raise AuthError({
            "code": "invalid_claims",
            "description": "'permissions' not included in JWT."
        }, 401)

    if permission not in payload["permissions"]:
        raise AuthError({
            "code": "forbidden",
            "description": "Permission not found."
        }, 403)

    return True


def requires_auth(auth_header, permission=""):
    token = get_token_from_auth_header(auth_header)
    payload = verify_decode_jwt(token)
    check_permissions(permission, payload)
    return payload
