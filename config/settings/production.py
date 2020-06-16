"""
Django settings for config project in local repository.
"""
import os
from .base import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Local SECRET_KEY
SECRET_KEY = os.environ["SECRET_KEY"]

# Allow debug
DEBUG = False

# Computer adress in the local network
ALLOWED_HOSTS = ["guillaume-ojardias.herokuapp.com"]
