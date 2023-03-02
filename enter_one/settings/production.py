# Parse database configuration from $DATABASE_URL
import dj_database_url
import os

from .base import *

ALLOWED_HOSTS = ['yourproject.example.com']

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = os.environ['STATIC_ROOT']
