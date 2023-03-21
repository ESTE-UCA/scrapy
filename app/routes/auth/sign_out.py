from . import auth
from flask import make_response
from app.configs import Config

@auth.route("/signout", methods=["POST", "GET"])
def signout():
    # set auth token session or cookie to null and return an empty response
    res = make_response({})
    res.set_cookie(Config.USER_TOKEN_KEY, "", httponly=True, samesite="strict", max_age=0)


    return res, 200