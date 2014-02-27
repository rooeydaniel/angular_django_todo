DEBUG = True
SANDBOX = True
TEMPLATE_DEBUG = DEBUG

DEBUG = True
SANDBOX = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'angular_todo_app',
        'USER': 'dstephenson',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

ALLOWED_HOSTS = ['localhost']