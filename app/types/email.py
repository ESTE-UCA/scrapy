from __future__ import annotations
from typing import Optional, Union
from app.errors import InputError, ErrorMessage, ErrorHint
from app.constants.error_msg_keys import ErrorMessageKey as mKey
from app.utils.validator import Validator
from .value import Value

class Email(Value[str]):
    key = "email"

    def __init__(self, value: str) -> None:
        super().__init__(self.key, value)

    @classmethod
    def create(cls, value: Optional[str] = None) -> Email | InputError:
        if value is None or value.strip().isspace():
            return InputError(cls.key, ErrorMessage.of(mKey.EMAIL_MSG_EMPTY), ErrorHint.of(mKey.EMAIL_HINT_EMPTY))
        
        value = value.lower().strip()
        if not Validator.isEmail(value):
            return InputError(cls.key, ErrorMessage.of(mKey.EMAIL_MSG_INVALID), ErrorHint.of(mKey.EMAIL_HINT_INVALID))
        
        return Email(value)
    
