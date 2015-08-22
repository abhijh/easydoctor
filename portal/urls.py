from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^registerDoctor/', views.registerDoctor, name='registerDoctor'),
    url(r'^showDoctor/(?P<doctorId>[0-9]+)/$', views.showDoctor, name='showDoctor'),
]