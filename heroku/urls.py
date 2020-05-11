from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('', views.index),
    path('login/',views.login),
    path('submitlogin',views.submitlogin),
    path('contact/',views.contact),
]
urlpatterns+=staticfiles_urlpatterns()
