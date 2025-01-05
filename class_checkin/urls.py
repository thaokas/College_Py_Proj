from class_checkin import views
from django.urls import path

app_name = 'checkin'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.checkin_result, name='checkin_result'),
]
