from typing import Optional
from .input_error import InputError, ErrorMessage


class ValidationError(Exception):
    def __init__(self, inputErrors: list[InputError], message: Optional[ErrorMessage] = None) -> None:
        super().__init__(message)
        self.message = message
        self.inputErrors = inputErrors

    def serialize(self) -> dict[str, any]:
        return {
            "message": self.message.serialize() if self.message is not None else "a validation error occurred",
            "details": [
                error.serialize()
                for error in self.inputErrors
            ],
        }