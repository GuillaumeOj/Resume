# Import the base settings
from .base import *


ALLOWED_HOSTS = ["*"]


SECRET_KEY = "-$-%s(l4f_cqx0wx0ima9f(n058^#h@81o5je^z1y1sal^a+!="
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
