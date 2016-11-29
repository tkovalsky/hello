from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail, name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$', views.edit_thing, name='edit_thing'),
    url(r'^admin/', admin.site.urls),
    ]
