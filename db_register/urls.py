from db_register import views
from django.urls import path

app_name = 'register'
urlpatterns = [
    path('student/', views.student_register, name='student_register'),
    path('course/', views.class_register, name='class_register'),
    path('enrollment/', views.course_enroll, name='course_enroll'),
]