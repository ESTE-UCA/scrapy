


class ErrorMessageKey(dict):
    # FORMAT: (input key cap)_(kind cup)_(for cap [1 = space or underscore])
    # key example: "email", "password", "username"
    # kind example: "msg", "hint", "reason", "warning"
    # for example: "empty", "invalid", "unauthorized", "vulnerable"
    USER1CREDENTIAL_MSG_INVALID = "user&credential_msg_invalid"
    USER1CREDENTIAL_MSG_TAKEN = "user&credential_msg_taken"
    USERNAME_MSG_EMPTY = "username_msg_empty"
    USERNAME_HINT_EMPTY = "username_hint_empty"
    USERNAME_MSG_INVALID = "username_msg_invalid"
    USERNAME_HINT_INVALID = "username_hint_invalid"
    USERNAME_REASON_TOO1LONG = "username_reason_too&long"
    EMAIL_MSG_TAKEN = "email_msg_taken"
    EMAIL_REASON_TAKEN = "email_reason_taken"
    EMAIL_HINT_TAKEN = "email_hint_taken"
    EMAIL_MSG_EMPTY = "email_msg_empty"
    EMAIL_HINT_EMPTY = "email_hint_empty"
    EMAIL_MSG_INVALID = "email_msg_invalid"
    EMAIL_HINT_INVALID = "email_hint_invalid"
    PASSWORD_MSG_EMPTY = "password_msg_empty"
    PASSWORD_HINT_EMPTY = "password_hint_empty"
    PASSWORD_MSG_INVALID = "password_msg_invalid"
    PASSWORD_HINT_INVALID = "password_hint_invalid"
    PASSWORD_REASON_STRENGTH = "password_reason_strength"
    PASSWORD_REASON_TOO1SHORT = "password_reason_too&short"
    PASSWORD_REASON_TOO1LONG = "password_reason_too&long"
    PASSWORD_REASON_MISS1UPPER = "password_reason_missed&uppercase"
    PASSWORD_REASON_MISS1LOWER = "password_reason_missed&lowercase"
    PASSWORD_REASON_MISS1DIGIT = "password_reason_missed&digit"
    PASSWORD_REASON_MISS1SYMBOL = "password_reason_missed&symbol"


