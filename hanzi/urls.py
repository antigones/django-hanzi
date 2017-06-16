from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hanzi_list, name='hanzi_list'),
	url(r'^test/cards/(?P<pk>[0-9]+)/$', views.test_card_list, name='test_card_list'),
]