"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@e3_f$45btsmgsxlsrs0cemgcnq@htw+*)3r%a1z&mm2ot^-ig"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    # The Django built-in application for controling login, logout in Django
    # it authenticate users for us
    # List of all the built-in URLs from Django's auth app:
    # 0. admin/
    # 1. login/ [name='login']
    # 2. logout/ [name='logout']
    # 3. password_change/ [name='password_change']
    # 4. password_change/done/ [name='password_change_done']
    # 5. password_reset/ [name='password_reset']
    # 6. password_reset/done/ [name='password_reset_done']
    # 7. reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # 8. reset/done/ [name='password_reset_complete']
    "django.contrib.auth",
    
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Installed 3rd party apps by Edmon
    "debug_toolbar",
    # cripsy-form is used to improve the UI of the form
    "crispy_forms",
    "crispy_tailwind",

    # Created Apps by Edmon.
    # The default website for the project
    "website",
    # "users"; the app that will handle users' sign-in, sign-up, registeration
    # and creating new accounts on the website
    "users",  # This is the "Sign Up Page" for creating new user accounts
]

MIDDLEWARE = [
    # Middlewares Added by Edmon
    "debug_toolbar.middleware.DebugToolbarMiddleware",


    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'v2_documents_managment_project_db1',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Custom Configurations and Settings addedy by Edmon:

# Configure Internal IPs
# The Debug Toolbar is shown only if your IP address is listed
# in Django’s INTERNAL_IPS setting. This means that for local development,
# you must add "127.0.0.1" to INTERNAL_IPS. You’ll need to create
# this setting if it doesn’t already exist in your settings module:

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Telling Django to use the crispy form template for tailwind-css library
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"


# These are the custom login and logout redirects for
# users accounts.
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
