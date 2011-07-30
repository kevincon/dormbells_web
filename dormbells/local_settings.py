import os.path

PROJECT_ROOT = '/home/kevin/dormbells2/repo/dormbells/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dormbells',                      # Or path to database file if using sqlite3.
        'USER': 'kevin',                      # Not used with sqlite3.
        'PASSWORD': 'mysqlpass',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


