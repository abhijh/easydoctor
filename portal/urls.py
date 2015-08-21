from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^registerDoctor/', views.registerDoctor, name='registerDoctor'),
    url(r'^showDoctor/(?P<doctorId>[0-9]+)/$', views.showDoctor, name='showDoctor'),
]