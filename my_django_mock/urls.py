# my_django_mock/urls.py

from django.contrib import admin
from django.urls import path
from mock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('new-tab/', views.new_tab_view, name='new_tab'),
]
