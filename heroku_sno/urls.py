from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^ukbooking/', include('ukbooking.urls')),
                       url(r'^$', redirect_to, {'url':'/ukbooking/'}),
                       url(r'^admin/', include(admin.site.urls)),
)
