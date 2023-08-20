import falcon
from jose import jwt

SECRET_KEY = "de3d973e375affa76a4d1e4611a2d6642729750809a30012c38c6f8b9f6f8cd2" # Update with your secret key
ALGORITHM = "HS256"  # Update with your chosen algorithm

def require_token(req, resp, resource, params):
    token = req.get_header("Authorization")
    if not token:
        raise falcon.HTTPUnauthorized(description="Authentication token is required")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        req.context["user"] = payload
    except jwt.JWTError:
        raise falcon.HTTPUnauthorized(description="Invalid token")

class AuthMiddleware:
    def process_resource(self, req, resp, resource, params):
        if getattr(resource, "requires_auth", True):
            require_token(req, resp, resource, params)




