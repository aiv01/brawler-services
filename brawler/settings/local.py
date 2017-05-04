from brawler.settings.base import *
import socket


ALLOWED_HOSTS = ('localhost', '127.0.0.1', 'testserver')
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True
USE_DEBUG_TOOLBAR = True
INTERNAL_IPS = ('127.0.0.1', socket.gethostbyname(''))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Add 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'brawler_2',  # '/path/example.db'. Path to database file if using sqlite3.
        'USER': 'aiv',  # Not used with sqlite3.
        'PASSWORD': 'aiv01',  # Not used with sqlite3.
        'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
    }
}

if USE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    SHOW_TOOLBAR_CALLBACK = True

CLONEDIGGER_CONFIG = {
    'IGNORE_DIRS': ['brawler', 'migrations']
}
