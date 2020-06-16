"""
Django settings for config project in local repository.
"""
from .base import *

import os

# Local SECRET_KEY
SECRET_KEY = "-$-%s(l4f_cqx0wx0ima9f(n058^#h@81o5je^z1y1sal^a+!="

# Allow debug
DEBUG = True

# Computer adress in the local network
ALLOWED_HOSTS = ["192.168.1.47"]
