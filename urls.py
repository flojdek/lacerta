from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^robots.txt', 'django.views.static.serve', {'path': /robots.txt, 'document_root': settings.MEDIA_ROOT, 'show_indexes': False}), 
	(r'^$', 'lacerta.onas.views.index'),
	(r'^onas/$', 'lacerta.onas.views.index'),
	(r'^oferta/(?P<type>\w*)$', 'lacerta.oferta.views.index'),
	(r'^publikacje/$', 'lacerta.publikacje.views.index'),
	(r'^doswiadczenie/$', 'lacerta.doswiadczenie.views.index'),
	(r'^wspolpraca/$', 'lacerta.wspolpraca.views.index'),
	(r'^kontakt/$', 'lacerta.kontakt.views.index'),
    # Example:
    # (r'^lacerta/', include('lacerta.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
