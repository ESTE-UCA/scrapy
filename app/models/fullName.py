from __future__ import annotations

class FullName:
    def __init__(self, firstName: str, middleNames: list[str], lastName: str) -> None:
        self.firstName = firstName
        self.middleNames = middleNames
        self.lastName = lastName

    def fromOriginJson(json: dict[str, any]) -> FullName:
        return FullName(firstName=json["firstName"],middleNames=json["middleNames"], lastName=json["lastName"])
    
    def serialize(self) -> dict[str, any]:
        return {
            "firstName": self.firstName,
            "middleNames": self.middleNames,
            "lastName": self.lastName
        }
    
    def __repr__(self) -> str:
        return f"<FullName firstName={self.firstName} middleNames={self.middleNames} lastName={self.lastName}>"