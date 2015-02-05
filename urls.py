from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
from easy_pdf.views import PDFTemplateView
import settings
from settings import OUR_APPS

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ECX.views.home', name='home'),
    # url(r'^ECX/', include('ECX.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    
)

urlpatterns += patterns('home.views',url(r'^$', 'home'),)

for app in settings.OUR_APPS:   
    urlpatterns += patterns('',url(r'^'+app+'/', include(app+'.urls',app_name=app)),)
    

if settings.DEBUG:
    urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.MEDIA_ROOT}),
                    )
    
# To provide admin UI on server this is static url

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.BASE_DIR, 'templates/static')}),

                    )