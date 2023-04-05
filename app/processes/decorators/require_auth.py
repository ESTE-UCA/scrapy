from functools import wraps
from flask import request
from werkzeug.exceptions import Unauthorized

def require_authentication(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        currentuser = request.environ["currentuser"]
        if currentuser is None:
            raise Unauthorized("A sign in/up is obligatory to perform this action")
        return f(*args, **kwargs)
    return decorator