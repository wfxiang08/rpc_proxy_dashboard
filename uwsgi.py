# -*- coding:utf-8 -*-
import os
import sys
from _project_env import PROJECT_NAME

PROJECT_ROOT = os.path.dirname(__file__)

# 创建log目录
log_paths = [os.path.join(PROJECT_ROOT, "log"), os.path.join(PROJECT_ROOT, "log/uwsgi/")]
for log_path in log_paths:
    if not os.path.exists(log_path):
        os.mkdir(log_path)

activate_this = os.path.join(PROJECT_ROOT, "..", "ENV_%s" % PROJECT_NAME, "bin/activate_this.py")
activate_this = os.path.abspath(activate_this)

if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))
else:
    raise Exception("virtual env not found at: %s" % activate_this)

# 只要uwsgi启动了，其他的代码就能自动找到
if not os.path.dirname(__file__) in sys.path[:1]:
    sys.path.insert(0, os.path.dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'



from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
