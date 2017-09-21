from django.conf.urls import url
from baseapp.views import *


app_name = 'baseapp'
urlpatterns = [
    url(r'^$', Index_FR.as_view(), name='home'),
]