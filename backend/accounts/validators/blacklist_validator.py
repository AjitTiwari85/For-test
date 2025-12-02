from .base import BaseValidator, PasswordValidationError

class BlacklistValidator(BaseValidator):
    def __init__(self, blacklist=None, **options):
        super().__init__(blacklist=blacklist or [], **options)
        self.blacklist = [p.lower() for p in self.options.get("blacklist", [])]

    def validate(self, password: str, user=None):
        if (password or "").lower() in self.blacklist:
            raise PasswordValidationError("This password is too common or insecure.", code="blacklisted_password")

    def get_help_text(self):
        return "Avoid using common passwords."
