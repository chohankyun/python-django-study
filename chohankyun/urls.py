from django.conf.urls import url
from django.views.generic import TemplateView

from chohankyun.views import *

urlpatterns = [
    url(r'^$', ListUser.as_view(),),
    url(r'^form/$', TemplateView.as_view(template_name='chohankyun/user_form.html'), ),
    url(r'^create/$', CreateUser.as_view(), ),
    url(r'^update/id/(?P<pk>[-\w]+)/$', UpdateUser.as_view(), ),
    url(r'^delete/id/(?P<pk>[-\w]+)/$', DeleteUser.as_view(), ),
    url(r'^id/(?P<pk>[-\w]+)/$', DetailUser.as_view(), ),
]
