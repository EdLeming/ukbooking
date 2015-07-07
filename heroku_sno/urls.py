from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^ukbooking/', include('ukbooking.urls')),
                       url(r'^$', RedirectView.as_view(url='/ukbooking/')),
                       url(r'^admin/', include(admin.site.urls)),
)
