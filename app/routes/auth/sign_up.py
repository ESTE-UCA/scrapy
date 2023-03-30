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
from app.utils import AuthUtils

@auth.route("/signup", methods=["POST"])
@validate_sign_form
def signup(cred: UserCredential): 
    
    # check if a user with provided email already existed and return error if true
    existingUser = UserRepository.exists(email=cred.email.value)
    if existingUser:
        raise ValidationError([
            InputError(cred.email.key, ErrorMessage.of(errKey.EMAIL_MSG_TAKEN), [ErrorReason.of(errKey.EMAIL_REASON_TAKEN)], ErrorHint.of(errKey.EMAIL_HINT_TAKEN))
        ], ErrorMessage.of(errKey.USER1CREDENTIAL_MSG_TAKEN))
    
    # create new user and save it into db
    user = User.create(cred)
    savedUser = UserRepository.save(user=user)
    # check if the user is an admin user
    isAdmin = AuthUtils.isAdminUser(savedUser.payload())
    # send back response with status code of 201 and user object as payload 
    res = AuthUtils.userSignInRes(savedUser.serialize(isAdmin))
    return res, 201