# -*- coding:utf-8 -*-
from settings_common.settings_base import *
from settings_common.settings_dbs import DATABASES_TEST as DATABASES


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'sqlite3.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
from settings_common.settings_install_apps import *
ZK_HOSTS = "127.0.0.1:2181"