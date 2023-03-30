from . import auth
from app.utils import AuthUtils

@auth.route("/signout", methods=["POST", "GET"])
def signout():
    return AuthUtils.userSignOutRes(), 200