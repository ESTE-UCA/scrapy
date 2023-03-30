from app.types.password import PasswordStrength


class PasswordInputRules(object):
    PASSWORD_MIN_LENGTH: int=6
    PASSWORD_MAX_LENGTH: int=20
    PASSWORD_REQUIRE_SYMBOL: bool = False
    PASSWORD_REQUIRE_UPPERCASE: bool= False
    PASSWORD_REQUIRE_LOWERCASE: bool = False
    PASSWORD_REQUIRE_DIGIT: bool = False
    PASSWORD_MIN_STRENGTH: PasswordStrength = 2
    PASSWORD_VALIDATE_BY_STRENGTH: bool = False # if false validate password by rules
