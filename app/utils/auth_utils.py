from flask import Response, make_response
from app.configs import Config
from typing import Optional
import json
import jwt

class AuthUtils:
    def userSignInRes(serializedUser: dict[str, any]) -> Response:
        response = make_response({"currentuser": serializedUser})
        # generate a json web token
        token = jwt.encode(payload=serializedUser, key=Config.JWT_KEY, algorithm="HS256")
        # store it in session or a cookie
        response.set_cookie(Config.USER_TOKEN_KEY, token, httponly=True, samesite="strict")
        return response
    
    def userSignOutRes()-> Response:
        # set auth token session or cookie to null and return an empty response
        response = make_response({
            "currentuser": None
        })
        response.set_cookie(Config.USER_TOKEN_KEY, "", httponly=True, samesite="strict", max_age=0)
        return response

    def isAdminUser(payload: dict[str, any]) -> bool:
        payloads = json.loads(Config.ADMINS_PAYLOADS)
        if type(payloads) is not list: return False
        
        return payloads.__contains__(payload)