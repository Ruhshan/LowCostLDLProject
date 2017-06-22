import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#local pg
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lipidproject',
        'USER': 'lipidprojectuser',
        'PASSWORD': 'shabashferoz',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True