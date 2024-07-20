# my_django_mock/urls.py

from django.contrib import admin
from django.urls import path
from mock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('iframe/', views.iframe, name='iframe'),
    path('new-tab-post/', views.new_tab_post_view, name='new_tab_post'),
    path('new-tab-get/', views.new_tab_get_view, name='new_tab_get'),
    path('new-tab-test/', views.new_tab_test_view, name='new_tab_test'),
    path('token-test/', views.token_test_view, name='token_test'),
]
