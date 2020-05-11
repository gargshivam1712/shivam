from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('', views.index),
    path('login/',views.login),
    path('submitlogin',views.submitlogin),
]
urlpatterns+=staticfiles_urlpatterns()
