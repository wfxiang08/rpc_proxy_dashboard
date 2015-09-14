# -*- coding:utf-8 -*-

import logging
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_ETAGS = True

STATIC_ROOT = PROJECT_ROOT + '/static/'
STATIC_URL = '/static/'



ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates',
)


SECRET_KEY = 'dasdsds#(4%x)ey((8sdasdk=g+sdasda$1'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)


LOGS_BASE_DIR = os.path.join(PROJECT_ROOT, "log")
if not os.path.exists(LOGS_BASE_DIR):
    os.mkdir(LOGS_BASE_DIR)


# 只要执行就OK
logging.root = logging.getLogger('default_logger')



# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
)
