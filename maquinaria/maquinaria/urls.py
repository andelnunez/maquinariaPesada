from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'manager.views.index'),
    # url(r'^maquinaria/', include('maquinaria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url('^nueva_maquinaria/$', 'manager.views.nueva_maquinaria'),
    url('^nuevo_banner/$', 'manager.views.nuevo_banner'),
    url('^cerrar_sesion/$', 'manager.views.cerrar_sesion'),
)
