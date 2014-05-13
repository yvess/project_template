# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function  # python3
from __future__ import unicode_literals, division  # python3
import warnings
warnings.filterwarnings(
        'error', r"DateTimeField received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

# postgres settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': "xx",
#         'USER': 'xx',
#         'PASSWORD': 'xx',
#         'HOST': 'xx',
#         'PORT': '5432',
#         'CONN_MAX_AGE': 60,
#         #'OPTIONS': {'autocommit': True}
#     }
# }

# sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CMD_RUNSERVER = "runserver_plus"
