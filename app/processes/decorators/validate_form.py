from functools import wraps
from flask import request
from app.types.user_credential import UserCredential

from app.types.email import Email
from app.types.password import Password
from app.types.username import Username

def validate_signup_form(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        email = Email.create(None if "email" not in request.form else request.form['email'])
        password = Password.create(None if "password" not in request.form else request.form['password'])
        username = Username.create(None if "username" not in request.form else request.form['username'])
        
        userCred = UserCredential.validateForSignUp(email, password, username)
        
        return f(userCred, *args, **kwargs)
    return decorator


def validate_signin_form(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        email = Email.create(None if "email" not in request.form else request.form['email'])
        password = Password.create(None if "password" not in request.form else request.form['password'])
        
        userCred = UserCredential.validateForSignUp(email, password)
        
        return f(userCred, *args, **kwargs)
    return decorator
