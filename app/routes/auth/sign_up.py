from . import auth
from flask import make_response
from werkzeug.exceptions import BadRequest
from app.repositories.user_repo import UserRepository
from app.models.user import User
import jwt
from app.configs import Config
from app.types.user_credential import UserCredential
from app.processes.decorators.validate_form import validate_sign_form
from app.errors import ValidationError, InputError, ErrorMessage, ErrorReason, ErrorHint
from app.constants import ErrorMessageKey as errKey

@auth.route("/signup", methods=["POST"])
@validate_sign_form
def signup(cred: UserCredential): 
    
    # check if a user with provided email already existed and return error if true
    existingUser = UserRepository.exists(email=cred.email.value)
    if existingUser:
        raise ValidationError([
            InputError(cred.email.key, ErrorMessage.of(errKey.EMAIL_MSG_TAKEN), ErrorReason.of(errKey.EMAIL_REASON_TAKEN), ErrorHint.of(errKey.EMAIL_HINT_TAKEN))
        ], ErrorMessage.of(errKey.USER1CREDENTIAL_MSG_TAKEN))
    
    # create new user and save it into db
    savedUser = UserRepository.save(user=User.create(cred))
    
    # generate a json web token
    userToken = jwt.encode(payload=savedUser.payload(), key=Config.JWT_KEY, algorithm="HS256")
    # store it in session or a cookie
    res = make_response(savedUser.dto())
    res.set_cookie(Config.USER_TOKEN_KEY, userToken, secure=True, samesite="strict")
    # send back response with status code of 201 and user object as payload 
    return res, 201