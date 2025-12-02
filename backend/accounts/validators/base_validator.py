from importlib import import_module
from django.conf import settings

class PasswordValidationError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

class BaseValidator:
    """
    Validators should inherit this and implement:
      - __init__(**options)
      - validate(password, user=None)  -> raise PasswordValidationError on failure
      - get_help_text()
    """
    def __init__(self, **options):
        self.options = options or {}

    def validate(self, password: str, user=None):
        raise NotImplementedError()

    def get_help_text(self):
        return ""

def load_validators():
    """
    Load enabled validators declared in settings.PASSWORD_VALIDATORS.
    Returns list of instances.
    """
    validators = []
    for entry in getattr(settings, "PASSWORD_VALIDATORS", []):
        enabled = entry.get("ENABLED", True)
        if not enabled:
            continue
        class_path = entry.get("CLASS")
        options = entry.get("OPTIONS", {}) or {}
        if not class_path:
            continue
        module_path, class_name = class_path.rsplit(".", 1)
        module = import_module(module_path)
        cls = getattr(module, class_name)
        validators.append(cls(**options))
    return validators

