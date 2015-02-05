from django.conf.urls import patterns, url

urlpatterns = patterns('home.views',
                        url(r'^invoice_generate/(?P<invid>\d+)$', 'invoice_generate'),
                        url(r'^home/$', 'home'),
                        url(r'^customers/$', 'customers'),
                        url(r'^pdf/$', 'some_view'),

                       )