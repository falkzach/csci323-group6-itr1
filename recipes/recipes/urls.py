from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

from main import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(urls)),
    url(r'^', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
)
