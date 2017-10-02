from django.conf.urls import url
from baseapp.views import *


app_name = 'baseapp'
urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^home/$', Home.as_view()),
]