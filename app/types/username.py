from __future__ import annotations
from typing import Optional
from app.errors import InputError, ErrorMessage, ErrorHint
from app.constants.error_msg_keys import ErrorMessageKey as mKey
from app.utils.validator import Validator
from .value import Value

class Username(Value[str]):
    key = "username"

    def __init__(self, value: str) -> None:
        super().__init__(self.key, value)

    @classmethod
    def create(cls, value: Optional[str] = None) -> Username | InputError:
        if value is None or value.strip().isspace():
            return InputError(cls.key, ErrorMessage.of(mKey.USERNAME_MSG_EMPTY), ErrorHint.of(mKey.USERNAME_MSG_EMPTY))
        
        value = value.lower().strip()
        if not Validator.isProperUsername(value):
            return InputError(cls.key, ErrorMessage.of(mKey.USERNAME_MSG_INVALID), ErrorHint.of(mKey.USERNAME_HINT_INVALID))
        
        return Username(value)