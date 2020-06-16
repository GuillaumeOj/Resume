"""
Django settings for config project in local repository.
"""
import os
from .base import *

# Local SECRET_KEY
SECRET_KEY = os.environ["SECRET_KEY"]

# Allow debug
DEBUG = False

# Computer adress in the local network
ALLOWED_HOSTS = ["guillaume-ojardias.herokuapp.com"]
