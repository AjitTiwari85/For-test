from .validators.base import load_validators, PasswordValidationError

def validate_password_server_side(password: str, user=None):
    """
    Run all enabled validators and return list of errors (empty list if OK).
    """
    errors = []
    validators = load_validators()
    for v in validators:
        try:
            v.validate(password, user=user)
        except PasswordValidationError as exc:
            errors.append({"message": exc.message, "code": exc.code, "validator": v.__class__.__name__})
    return errors
