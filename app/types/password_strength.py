from enum import IntEnum 

class PasswordStrength(IntEnum):
    FRAGILE = 0
    WEAK = 1
    MODERATE = 2
    STRONG = 4
    MIGHTY = 5
