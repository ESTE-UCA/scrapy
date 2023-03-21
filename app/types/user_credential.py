from __future__ import annotations
from .email import Email
from .password import Password
from app.errors import InputError, ValidationError, ErrorMessage
from app.constants import ErrorMessageKey as errKey


class UserCredential:
    def __init__(self, email: Email, password: Password) -> None:
        self.email = email
        self.password = password

    @classmethod
    def validate(self, email: Email | InputError, password: Password | InputError) -> UserCredential:
        errors: list[InputError] = []
        if type(email) is InputError:
            errors.append(email)
        elif type(password) is InputError:
            errors.append(password)
        
        if errors.__len__() > 0:
            raise ValidationError(errors, message=ErrorMessage.of(errKey.USER1CREDENTIAL_MSG_INVALID))
        
        return UserCredential(email, password)
        
    def serialize(self)-> dict[str, any]:
        return {
            "email": self.email.value,
            "password": self.password.value
        }