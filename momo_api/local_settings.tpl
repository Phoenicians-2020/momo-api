# Configurable Settings
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = 'localhost'

SECRET_KEY = '^6r9*4he)(16da%0qpz(=0x^^=c814i)rz8#ek%cq6^qq87wkk'

DEBUG = True

DATABASES = {
    # Ends with "postgresql", "mysql", "sqlite3" or "oracle".
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    },
}

# INSTALLED_APPS += ['django_extensions']

# if DEBUG_TOOLBAR:
#     INSTALLED_APPS = [
#         'debug_toolbar',
#     ] + INSTALLED_APPS

#     MIDDLEWARE = [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ] + MIDDLEWARE


# EMAIL BACKEND
# https://docs.djangoproject.com/en/2.1/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


# Django Session Security
# https://django-session-security.readthedocs.io/en/latest/full.html
SESSION_SECURITY_WARN_AFTER = 540
SESSION_EXPIRE_AFTER = 600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# AWS S3 Credentials
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '<insert-access-key-id-here>'
AWS_SECRET_ACCESS_KEY = '<insert-secret-access-key-here>'
AWS_STORAGE_BUCKET_NAME = '<insert-bucket-name-here>'
AWS_S3_REGION_NAME = '<insert-s3-region-name-here>'
