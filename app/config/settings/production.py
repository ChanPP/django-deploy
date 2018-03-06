from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
]
DATABASES = secrets['DATABASES']
WSGI_APPLICATION = 'config.wsgi.production.application'
