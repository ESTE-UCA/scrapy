

from functools import wraps
from flask import request
from werkzeug.exceptions import Unauthorized

def require_author_confirmation(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        currentuser = request.environ["currentuser"]
        if not currentuser["isConfirmed"]:
            raise Unauthorized("accessing papers requires author confirmation")
        return f(*args, **kwargs)
    return decorator