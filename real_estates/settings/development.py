from .base import *

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