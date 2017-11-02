
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('overview.urls')),
    url(r'^wish/', include('wish.urls')),
    url(r'^todo/', include('todo.urls')),
    url(r'^admin/', admin.site.urls),
]
