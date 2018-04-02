from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cms.views.pagina_inicio'),
    url(r'^create/(.*)/(.*)$', 'cms.views.createPage'),
    url(r'^web/(\d+)$', 'cms.views.showContent'),
    url(r'^admin/', include(admin.site.urls)),
)
