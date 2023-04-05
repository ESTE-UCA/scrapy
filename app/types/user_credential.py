from __future__ import annotations
from typing import Optional
from .email import Email
from .password import Password
from .username import Username
from app.errors import InputError, ValidationError, ErrorMessage
from app.constants import ErrorMessageKey as errKey


class UserCredential:
    def __init__(self, email: Email, password: Password, username: Optional[Username] = None) -> None:
        self.username = username
        self.email = email
        self.password = password

    
    @classmethod
    def validateForSignUp(self, email: Email | InputError, password: Password | InputError, username: Optional[Username | InputError] = None) -> UserCredential:
        errors: list[InputError] = []
        if type(email) is InputError:
            errors.append(email)
        elif type(password) is InputError:
            errors.append(password)
        elif username is not None and type(username) is InputError:
            errors.append(username)
        
        
        if errors.__len__() > 0:
            raise ValidationError(errors, message=ErrorMessage.of(errKey.USER1CREDENTIAL_MSG_INVALID))
        
        return UserCredential(email, password, username)
        
    def serialize(self)-> dict[str, any]:
        return {
            "email": self.email.value,
            "password": self.password.value,
            "username": self.username.value
        }