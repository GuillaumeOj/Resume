"""
Django settings for config project in local repository.
"""
from .base import *  # noqa: F401, F403


# Local SECRET_KEY
SECRET_KEY = "-$-%s(l4f_cqx0wx0ima9f(n058^#h@81o5je^z1y1sal^a+!="

# Allow debug
DEBUG = True

# Computer adress in the local network
ALLOWED_HOSTS = ["*"]

# Local database his sqlite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}
