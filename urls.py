from django.conf.urls import url
from baseapp.views import *


app_name = 'baseapp'
urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^home/$', Home.as_view()),
    url(r'^contactus/$', ContactUs.as_view(), name='contactus'),
    url(r'^reportbug/$', ReportBug.as_view(), name='reportbug'),
    url(r'^aboutus/$', AboutUs.as_view(), name='aboutus'),
    url(r'^legalinformation/$', LegalInformation.as_view(), name='legalinformation'),
    url(r'^presscenter/$', PressCenter.as_view(), name='press'),
    url(r'^partner/$', Partner.as_view(), name='partner'),
]
