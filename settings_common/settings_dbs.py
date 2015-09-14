# -*- coding:utf-8 -*-
import os

from settings_common.settings_base import PROJECT_ROOT


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'sqlite3_online.db'), # 其实不需要数据库
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },

}

