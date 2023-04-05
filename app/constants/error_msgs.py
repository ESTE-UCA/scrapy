from .error_msg_keys import ErrorMessageKey as mKey
from typing import Union



def error_msgs() -> dict[mKey, Union[str, list[str]]]:
    return {
        mKey.USER1CREDENTIAL_MSG_INVALID: "some fields need a second observation",
        mKey.USER1CREDENTIAL_MSG_TAKEN: "credentials specified might have already been taken",
        mKey.PASSWORD_MSG_EMPTY: "password field must have a value.",
        mKey.PASSWORD_HINT_EMPTY: "please enter a fairly strong password.",
        mKey.PASSWORD_MSG_INVALID: "this password is vulnerable (fragile) and easy to break",
        mKey.PASSWORD_HINT_INVALID: (                
            "an example of a strong password is: Bruh!34_sTe3d", 
            "a password with a combination of lower case (abc...), upper case (ABC...), special chars (-_@^$#...), and numbers (123...), with minimal length of 12 is called a titanium shield",
            "a titanium shield will take at least two millions years for hackers too brute force!"
        ),
        mKey.PASSWORD_REASON_STRENGTH: "password is not strong enough.",
        mKey.PASSWORD_REASON_TOO1SHORT: "password is too short.",
        mKey.PASSWORD_REASON_TOO1LONG: "password is too long",
        mKey.PASSWORD_REASON_MISS1DIGIT: "password is missing at least one digit (123...)",
        mKey.PASSWORD_REASON_MISS1SYMBOL: "password is missing at least one symbol (!-_@^$#...)",
        mKey.PASSWORD_REASON_MISS1UPPER: "password is missing at least one capital letter (ABC...)",
        mKey.PASSWORD_REASON_MISS1LOWER: "password is missing at least one lowercase letter (abc...)",
        mKey.EMAIL_MSG_EMPTY: "email address field must have a value.",
        mKey.EMAIL_HINT_EMPTY: "please enter a valid email address.",
        mKey.EMAIL_MSG_INVALID: "email address has wrong format.",
        mKey.EMAIL_HINT_INVALID: (
            "an example of a valid email address is: username@example.com.", 
        ),
        mKey.EMAIL_MSG_TAKEN: "email is already in use.",
        mKey.EMAIL_REASON_TAKEN: "a user with the email entered is already exist.",
        mKey.EMAIL_HINT_TAKEN: (
            "check email's spelling to assure it is yours.",
            "try to sign in instead of creating new user.",
            "use different email address as current is already being used.",
            "if the email is yours and you haven't signed up in this website before. feel free to contact us on [oussamamakouar@gmail.com] and report a potential fraud or scam."
        ),
        mKey.USERNAME_MSG_EMPTY: "username field must have a value",
        mKey.USERNAME_HINT_EMPTY: "please enter your full name (example: Elarbi Rodriguez)",
        mKey.USERNAME_MSG_INVALID: "please enter a proper username (no digits)",
        mKey.USERNAME_HINT_INVALID: "only computers and non living get labeled by numbers"

    }   

def error_msg(key: mKey):
    return error_msgs().get(key)