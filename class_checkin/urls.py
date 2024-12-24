from django.urls import path
from . import views

app_name = 'checkin'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('result/', views.result, name='result'),
    path('register_success/', views.register_success, name='register_success'),
    path('register_fail/', views.register_fail, name='register_fail'),
]