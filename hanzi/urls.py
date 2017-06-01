from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hanzi_list, name='hanzi_list'),
]