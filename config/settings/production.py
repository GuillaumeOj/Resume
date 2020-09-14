"""Django settings for the remote project."""
import os

import dj_database_url
from dotenv import find_dotenv
from dotenv import load_dotenv

# Import the base settings
from .base import *


ALLOWED_HOSTS = ["ojardias.io", "guillaume.ojardias.io", "www.ojardias.io"]

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True if os.getenv("DEBUG") == "True" else False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}
