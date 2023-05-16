from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
]


if settings.DEBUG:
    urlpatterns += [
      path(r'^media/(?P<path>.*)$', serve),
      path(r'^static/(?P<path>.*)$', serve),
    ]

admin.site.site_header = 'Администрирование электронного журнала'