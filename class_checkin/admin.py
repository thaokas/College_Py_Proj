from django.contrib import admin

from class_checkin.models import Student, Course, Enrollment

# Register your models here.
admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(Student)

# class StudentAdmin(admin.ModelAdmin):
