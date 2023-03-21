from typing import Optional, Union
from app.constants import ErrorMessageKey, error_msg
from abc import abstractmethod

class ErrorMessage:
    def __init__(self, key: ErrorMessageKey, msg: str) -> None:
        self.key = key
        self.msg = msg

    @classmethod
    def of(self, key: ErrorMessageKey):
        return ErrorMessage(key, error_msg(key))
    
    @abstractmethod
    def serialize(self) -> dict[str, str | list[str]]:
        return {
            "key": self.key,
            "message": self.msg
        }
    
    def __repr__(self) -> str:
        return f"an error occurred with key of [{self.key}] and message: {self.msg}.\n"
    


class ErrorReason(ErrorMessage):
    def __init__(self, key: ErrorMessageKey, msg: str) -> None:
        super().__init__(key, msg)
    
    def __repr__(self) -> str:
        return f"due to a reason with key of: {self.key}, and reason message of: {self.msg}.\n"
    

class ErrorHint(ErrorMessage):
    def __init__(self, key: str, msg: str) -> None:
        super().__init__(key, msg)

    def __repr__(self) -> str:
        return f"a hint with key [{self.key}] might helps you to overstep it: {self.msg}.\n"



class InputError:
    def __init__(self, key: str, message: ErrorMessage, reasons: Optional[list[ErrorReason]] = None,hint: Optional[ErrorHint]= None) -> None:
        self.key = key
        self.message = message
        self.hint = hint
        self.reasons = reasons

    def serialize(self) -> dict[str, any]:
        return {
            "key": self.key,
            "message": self.message.serialize(),
            "hint": self.hint.serialize() if self.hint is not None else None,
            "reasons": [
                reason.serialize()
                for reason in self.reasons
            ] if self.reasons is not None and len(self.reasons) > 0 else None
        }
    
    def __repr__(self) -> str:
        return f"on input with key of: {self.key}, {self.message}, {self.reasons}, {self.hint}"
    
