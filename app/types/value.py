from __future__ import annotations
from abc import abstractmethod, abstractproperty
from typing import Generic, TypeVar, Union, Optional
from app.errors.input_error import InputError
from app.constants.error_msgs import error_msgs

T = TypeVar("T", bound=object)
class Value(Generic[T]):
    key: str = "value"

    def __init__(self, key: str, value: T) -> None:
        self.key = key
        self.value = value

    @abstractmethod
    def create(value: Optional[T]) -> Union[Value[T], InputError]:
        raise NotImplemented()
    
    @abstractmethod
    def err_msg(key: str) -> str | list[str]:
        return error_msgs().get(key) or f"No error message associated to this key ${key}"

    @abstractmethod
    def __eq__(self, other: Value[T]) -> bool:
        if not isinstance(self, other): return False
        if self.value != other.value: return False
        return True
    
