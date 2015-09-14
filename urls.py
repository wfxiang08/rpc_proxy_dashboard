from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.home', name='home'),
)

urlpatterns += staticfiles_urlpatterns()

# urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)