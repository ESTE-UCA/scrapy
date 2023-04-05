from __future__ import annotations
from sqlalchemy.types import TypeDecorator, JSON



class FullName:
    def __init__(self, firstName: str, middleNames: list[str], lastName: str) -> None:
        self.firstName = firstName
        self.middleNames = middleNames
        self.lastName = lastName

    def fromOriginJson(json: dict[str, any]) -> FullName:
        return FullName(firstName=json["firstName"],middleNames=json["middleNames"], lastName=json["lastName"])
    
    def inline(self):
        middleNames = ""
        for name in self.middleNames:
            middleNames = str.join(middleNames, f" {name}")
        return f"{self.firstName}{middleNames} {self.lastName}"
    
    def serialize(self) -> dict[str, any]:
        return {
            "firstName": self.firstName,
            "middleNames": self.middleNames,
            "lastName": self.lastName
        }
    
    def __repr__(self) -> str:
        return f"<FullName firstName={self.firstName} middleNames={self.middleNames} lastName={self.lastName}>"


class FullNameField(TypeDecorator):
    impl = JSON

    def __repr__(self):
        return self.impl.__repr__()
    
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(JSON)

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        else:
            if isinstance(value, FullName):
                return value.serialize()

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return FullName.fromOriginJson(value)