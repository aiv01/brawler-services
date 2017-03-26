from brawler.settings.base import *

ALLOWED_HOSTS = ('dev.brawler.com',)

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Add 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'brawler_dev',  # '/path/example.db'. Path to database file if using sqlite3.
        'USER': 'aiv',  # Not used with sqlite3.
        'PASSWORD': 'aiv01',  # Not used with sqlite3.
        'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
    }
}

# Fab commands configuration
WORKING_DIR = "www/brawler_dev"
HOST_USER = "30248"
HOST_IP = ""
HOST_PORT = "22"
