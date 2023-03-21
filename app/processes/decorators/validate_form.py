from functools import wraps
from flask import request
from app.types.user_credential import UserCredential

from app.types.email import Email
from app.types.password import Password

def validate_sign_form(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        email = Email.create(None if "email" not in request.form else request.form['email'])
        password = Password.create(None if "password" not in request.form else request.form['password'])

        userCred = UserCredential.validate(email, password)
        
        return f(userCred, *args, **kwargs)
    return decorator
