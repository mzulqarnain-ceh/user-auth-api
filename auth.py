import jwt
from functools import wraps
from flask import request,jsonify
from config import SECRET_KEY
# Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=request.headers.get("Authorization")
        if token is None:
            return jsonify({"error":"Token is missing"}),401
        token=token.split(" ")[1]
        try:
            payload=jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error":"Token Expired"}),401
        except jwt.InvalidTokenError:
            return jsonify({"error":"Invalid token"}),401
        return f(payload, *args, **kwargs)
    return decorated
        