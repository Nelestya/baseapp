from django.urls import include, path
from . import views


app_name = 'baseapp'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('home/', views.Home.as_view()),
]
