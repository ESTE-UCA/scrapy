import validators
import re

class Validator:
    def hasUpper(value: str) -> bool:
        for i in range(0, len(value)):
            if value[i].isupper():
                return True
        return False
    
    def hasLower(value: str) -> bool:
        for i in range(0, len(value)):
            if value[i].islower():
                return True
        return False
    
    def hasDigits(value: str) -> bool:
        return re.search(r"\d", value) is not None

    def hasSymbols(value: str) -> bool:
        return re.search(r"\W", value) is not None
    
    def isEmail(value: str) -> bool:
        return validators.email(value)
    