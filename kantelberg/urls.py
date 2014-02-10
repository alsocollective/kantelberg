from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'product.views.home', name='home'),
    url(r'^about/$', 'product.views.home', name='home'),
    url(r'^media/(?P<article>.*)/$', 'product.views.press', name='home'),

    url(r'^projects/$', 'product.views.home', name='home'),
    url(r'^projects/(?P<project>.*)/$', 'product.views.project', name='home'),

    url(r'^products/$', 'product.views.home', name='home'),
    url(r'^products/(?P<product>.*)/$', 'product.views.productCat', name='home'),

    url(r'^whats-new/$', 'product.views.home', name='home'),

    url(r'^product/(?P<product>.*)/$', 'product.views.product', name='home'),


    url(r'^contact/$', 'product.views.home', name='home'),

    # url(r'^kantelberg/', include('kantelberg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
