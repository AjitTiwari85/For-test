import re
from .base import BaseValidator, PasswordValidationError

SPECIAL_RE = re.compile(r"[!@#$%^&*(),.?\":{}|<>_\-\\\[\]\/`~;']")

class CharacterValidator(BaseValidator):
    def __init__(self, require_upper=True, require_digit=True, require_special=True, **options):
        super().__init__(require_upper=require_upper, require_digit=require_digit, require_special=require_special, **options)
        self.require_upper = self.options.get("require_upper", True)
        self.require_digit = self.options.get("require_digit", True)
        self.require_special = self.options.get("require_special", True)

    def validate(self, password: str, user=None):
        if self.require_upper and not any(c.isupper() for c in (password or "")):
            raise PasswordValidationError("Password must contain at least one uppercase letter.", code="no_upper")
        if self.require_digit and not any(c.isdigit() for c in (password or "")):
            raise PasswordValidationError("Password must contain at least one digit.", code="no_digit")
        if self.require_special and not SPECIAL_RE.search(password or ""):
            raise PasswordValidationError("Password must contain at least one special character.", code="no_special")

    def get_help_text(self):
        parts = []
        if self.require_upper:
            parts.append("an uppercase letter")
        if self.require_digit:
            parts.append("a digit")
        if self.require_special:
            parts.append("a special character")
        return "Password must contain at least " + ", ".join(parts) + "."
