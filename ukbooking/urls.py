from django.conf.urls import patterns, url

from booking import views

urlpatterns = patterns('',
                       #url(r'^$', views.index, name='index'),

                       url(r'^apartments/$', views.Apartments.as_view(), name='apartments'),
                       url(r'^apartment/(?P<apartment_id>\d+)/$', views.apartment, name='apartment'),
)
