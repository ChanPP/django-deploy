from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = [
    '.amazonaws.com',
]
DATABASES = secrets['DATABASES']
WSGI_APPLICATION = 'config.wsgi.dev.application'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'