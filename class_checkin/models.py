from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    std_uid = models.IntegerField()
    std_name = models.CharField(max_length=50)
    std_info = models.TextField()

    def __str__(self):
        return str(self.std_uid) + self.std_name + str(self.std_info)


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()

    def __str__(self):
        return str(self.course_id) + self.course_name + str(self.course_period) + str(self.course_description)


class Enrollment(models.Model):
    enrollment_id = models.IntegerField(primary_key=True)
    Student_Id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course_Id = models.ForeignKey(Course, on_delete=models.CASCADE)
    Grade = models.IntegerField()

    def __str__(self):
        return str(self.Student_Id) + str(self.Course_Id) + str(self.Grade)
