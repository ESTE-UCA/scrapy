from __future__ import annotations
from app.errors import ErrorMessage, ErrorReason, ErrorHint, InputError
from app.utils import PasswordHasher, Validator
from .value import Value
from .password_strength import PasswordStrength
from typing import Optional
from app.constants import ErrorMessageKey as errKey
from app.configs.rules import PasswordInputRules as rules



class Password(Value[str]):
    key = "password"

    def __init__(self, value: str, isHashed: bool) -> None:
        super().__init__(self.key, value)
        self.isHashed = isHashed

    @classmethod
    def create(cls, value: Optional[str] = None, isHashed: bool = False, hash_it: Optional[bool] = False) -> Password | InputError:
        if(value is None):
            return InputError(cls.key, ErrorMessage.of(errKey.PASSWORD_MSG_EMPTY), ErrorHint.of(errKey.PASSWORD_HINT_EMPTY))
        
        if not isHashed:
            errReasons = cls.checkValidityByStrength(value) if rules.PASSWORD_VALIDATE_BY_STRENGTH else cls.checkValidityByRules(value)
            if(errReasons != None and len(errReasons) > 0): return InputError(cls.key, ErrorMessage.of(errKey.PASSWORD_MSG_INVALID), errReasons, ErrorHint.of(errKey.PASSWORD_HINT_INVALID))
            if hash_it: 
                value = PasswordHasher.toHash(value)
                isHashed = True

        return Password(value, isHashed)
    

    def checkValidityByRules(value: str) -> list[ErrorReason] | None:
        reasonsKeys: list[errKey] = []
        
        length = len(value)
        tooShort = length < rules.PASSWORD_MIN_LENGTH
        tooLong = length > rules.PASSWORD_MAX_LENGTH
        hasNoDigits = Validator.hasDigits(value) is False
        hasNoLowercase = Validator.hasLower(value) is False
        hasNoUppercase = Validator.hasUpper(value) is False
        hasNoSymbols = Validator.hasSymbols(value) is False

        if tooLong or tooShort:
            reasonsKeys.append(errKey.PASSWORD_REASON_TOO1LONG if tooLong else errKey.PASSWORD_REASON_TOO1SHORT)

        if hasNoDigits and rules.PASSWORD_REQUIRE_DIGIT:
            reasonsKeys.append(errKey.PASSWORD_REASON_MISS1DIGIT)
        
        if hasNoUppercase and rules.PASSWORD_REQUIRE_UPPERCASE:
            reasonsKeys.append(errKey.PASSWORD_REASON_MISS1UPPER)

        if hasNoLowercase and rules.PASSWORD_REQUIRE_LOWERCASE:
            reasonsKeys.append(errKey.PASSWORD_REASON_MISS1LOWER)

        if hasNoSymbols and rules.PASSWORD_REQUIRE_SYMBOL:
            reasonsKeys.append(errKey.PASSWORD_REASON_MISS1SYMBOL)

        return [
            ErrorReason.of(key)
            for key in reasonsKeys
        ] if len(reasonsKeys) > 0 else None


    def checkValidityByStrength(value: str) -> list[ErrorReason] | None:
        if Password.checkStrength(value) < rules.PASSWORD_MIN_STRENGTH:
            return [ErrorReason.of(errKey.PASSWORD_REASON_STRENGTH)]


    def checkStrength(value: str) -> PasswordStrength:
        # calculating the length
        length = len(value)
        # checking specs through regex
        hasNoDigits = Validator.hasDigits(value) is False
        hasNoLowercase = Validator.hasLower(value) is False
        hasNoUppercase = Validator.hasUpper(value) is False
        hasNoSymbols = Validator.hasSymbols(value) is False

        # checking specs combinations
        hasOnlyDigits = not hasNoDigits and hasNoLowercase and hasNoUppercase and hasNoSymbols
        hasOnlyLowercase = not hasNoLowercase and hasNoUppercase and hasNoDigits and hasNoSymbols
        hasOnlyUppercase = not hasNoUppercase and hasNoLowercase and hasNoDigits and hasNoSymbols
        hasOnlyUppersAndLowers = not hasNoLowercase and not hasNoUppercase and hasNoDigits and hasNoSymbols
        hasOnlyUppersAndLowersAndDigits = not hasNoLowercase and not hasNoUppercase and not hasNoDigits and hasNoSymbols
        hasOnlyUppersOrLowersAndDigits = (not hasNoLowercase or not hasNoUppercase) and not hasNoDigits and hasNoSymbols
        hasAllSpecs = not hasNoLowercase and not hasNoUppercase and not hasNoDigits and not hasNoSymbols

        if hasOnlyDigits:
            return PasswordStrength.FRAGILE if length <= 10 else PasswordStrength.WEAK if length <= 15 else PasswordStrength.MODERATE
        
        if hasOnlyLowercase or hasOnlyUppercase:
            return PasswordStrength.FRAGILE if length <= 7 else PasswordStrength.WEAK if length <= 10 else PasswordStrength.MODERATE \
                if length <= 13 else PasswordStrength.STRONG if length <= 17 else PasswordStrength.MIGHTY
        
        if hasOnlyUppersAndLowers or hasOnlyUppersOrLowersAndDigits:
            return PasswordStrength.FRAGILE if length <= 6 else PasswordStrength.WEAK if length <= 9 else PasswordStrength.MODERATE \
                if length <= 11 else PasswordStrength.STRONG if length <= 14 else PasswordStrength.MIGHTY
        
        if hasOnlyUppersAndLowersAndDigits: 
            return PasswordStrength.FRAGILE if length <= 5 else PasswordStrength.WEAK if length <= 8 else PasswordStrength.MODERATE \
                if length <= 10 else PasswordStrength.STRONG if length <= 13 else PasswordStrength.MIGHTY
        
        if hasAllSpecs:
            return PasswordStrength.FRAGILE if length <= 5 else PasswordStrength.WEAK if length <= 8 else PasswordStrength.MODERATE \
                if length <= 10 else PasswordStrength.STRONG if length <= 12 else PasswordStrength.MIGHTY
   