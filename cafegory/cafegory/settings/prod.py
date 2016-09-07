from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'cafegory'),
        'USER': os.environ.get('DJANGO_DATABASE_USER', 'ubuntu'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', 'google'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', '127.0.0.1'),
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAISLJLQCBN7FIMHCA'  # access key
AWS_SECRET_ACCESS_KEY = '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'  # secret access key
AWS_REGION = 'ap-northeast-2' ## Seoul Region
AWS_STORAGE_BUCKET_NAME = 'cofin'  # AWS S3 버켓 이름
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_SECURE_URLS = False ## https
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "http://%s/" % AWS_S3_CUSTOM_DOMAIN
