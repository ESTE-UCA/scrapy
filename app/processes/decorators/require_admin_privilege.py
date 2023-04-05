from functools import wraps
from flask import request
from werkzeug.exceptions import Unauthorized

def require_admin_privilege(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        currentuser = request.environ["currentuser"]
        if not currentuser["isAdmin"]:
            raise Unauthorized("only users with admin privilege have the authority to perform this action")
        return f(*args, **kwargs)
    return decorator