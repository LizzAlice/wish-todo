from django.conf.urls port urls

from . import views

urlpatterns = [
    url(r'$', views.wish_detail, name = 'wish-detail')
]
