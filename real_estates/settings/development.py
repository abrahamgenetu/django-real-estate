from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_ENCRYPTION=env("EMAIL_ENCRYPTION")
DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Real_estate',
        'USER': 'abraham', #default user name
        'PASSWORD': 'yoratorad@abraham3',
        'HOST': '127.0.0.1', # default host
        'PORT': '5432', # default postgres port
    }
}