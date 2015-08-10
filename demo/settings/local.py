# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from .base import *

DEBUG = True

# количество файлов, что может загрузить пользователь
MAX_USER_FILES_COUNT = 34
MAX_DAYS_TO_OLD = 365


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',

        'HOST': 'localhost',
        'PORT': '5432',
        'AUTOCOMMIT': True,
    },
    # 'default': {
    #      'ENGINE': 'django.db.backends.sqlite3',
    #      'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    # }

}