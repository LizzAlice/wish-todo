
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'overview'
urlpatterns = [
    url(r'', include('overview.urls')),
    url(r'^wish/', include('wish.urls')),
    url(r'^todo/', include('todo.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
