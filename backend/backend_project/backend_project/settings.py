import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "change-this-in-prod")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",
    "accounts",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ]},
    },
]

WSGI_APPLICATION = "backend_project.wsgi.application"
ASGI_APPLICATION = "backend_project.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []  # using custom validators in code instead of Django built-in

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"

# DRF - minimal config (adjust for production)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# CORS (dev convenience)
CORS_ALLOW_ALL_ORIGINS = True

# ---- Custom password validators configuration ----
# List of validators. Each entry: { "CLASS": "dot.path.ClassName", "OPTIONS": {...}, "ENABLED": True }
PASSWORD_VALIDATORS = [
    {
        "CLASS": "accounts.validators.length_validator.LengthValidator",
        "OPTIONS": {"min_length": 8},
        "ENABLED": True
    },
    {
        "CLASS": "accounts.validators.character_validator.CharacterValidator",
        "OPTIONS": {"require_upper": True, "require_digit": True, "require_special": True},
        "ENABLED": True
    },
    {
        "CLASS": "accounts.validators.blacklist_validator.BlacklistValidator",
        "OPTIONS": {"blacklist": ["password", "123456", "12345678", "qwerty", "test", "admin"]},
        "ENABLED": True
    },
]
# --------------------------------------------------

