from db_register import views
from django.urls import path

app_name = 'db_register'
urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student_register, name='student_register'),
    path('class', views.class_register, name='class_register'),
    path('enrollment', views.course_enroll, name='course_enroll'),
    path('student/success/', views.student_register_success, name='student_success'),
    path('student/fail/', views.student_register_fail, name='student_fail'),
    path('class/success/', views.class_register_success, name='class_success'),
    path('class/fail/', views.class_register_fail, name='class_fail'),
    path('enrollment/success/', views.course_enroll, name="enroll_success"),
    path('enrollment/fail/', views.course_enroll, name="enroll_fail"),
]