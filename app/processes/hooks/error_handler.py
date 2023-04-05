from flask import make_response
from werkzeug.exceptions import BadRequest, HTTPException
from app.errors.validation_error import ValidationError
from app.configs import Config


def handleExceptions(e: Exception):    
    if isinstance(e, ValidationError):
        res = make_response(
            e.serialize(),
            403
        )
        res.set_cookie(Config.USER_TOKEN_KEY, "", max_age=0, httponly=True)
        return res

    if(isinstance(e, BadRequest)):   
        res = make_response({
            "description": BadRequest().description,
            "message": e.description,
            "error": e.code,
        })
        res.set_cookie(Config.USER_TOKEN_KEY, "", max_age=0, httponly=True)
        return res
    
    if(isinstance(e, HTTPException)):
        res = make_response({
            "description": HTTPException().description,
            "message": e.description,
            "code": e.code,
        })
        return res, e.code
    

    return make_response({"error occurred": type(e).__repr__(e)})

    

