from django.conf.urls import url
from django.views.generic import TemplateView

from chohankyun.views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), ),
]
