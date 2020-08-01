"""
Django settings for config project in local repository.
"""
import os

import dj_database_url

from .base import *

# Local SECRET_KEY
SECRET_KEY = os.environ["SECRET_KEY"]

# Allow debug
DEBUG = False

# Computer adress in the local network
ALLOWED_HOSTS = ["guillaume-ojardias.herokuapp.com", ".ojardias.io"]

SECURE_SSL_REDIRECT = True


# Heroku database
DATABASE_URL = os.environ["DATABASE_URL"]
DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
