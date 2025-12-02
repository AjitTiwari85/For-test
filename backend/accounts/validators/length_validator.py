from .base import BaseValidator, PasswordValidationError

class LengthValidator(BaseValidator):
    default_min = 8

    def __init__(self, min_length=None, **options):
        super().__init__(min_length=min_length or self.default_min, **options)
        self.min_length = self.options.get("min_length", self.default_min)

    def validate(self, password: str, user=None):
        if not password or len(password) < self.min_length:
            raise PasswordValidationError(
                f"Password must be at least {self.min_length} characters long.",
                code="password_too_short"
            )

    def get_help_text(self):
        return f"Your password must contain at least {self.min_length} characters."
