import cv2
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from EasyCheckin.settings import FACE_EMBEDDING, VECTOR_DB_CLIENT, VECTOR_DB_NAME
from class_checkin.models import Student, Course, Enrollment


@api_view(['POST'])
def student_register(request):
    register_result = ""
    register_message = ""

    std_id = int(request.POST.get('std_id'))
    std_name = request.POST.get('std_name')

    if len(Student.objects.filter(std_uid=std_id)) != 0:
        register_result = "FAILED"
        register_message = "Student Already Registered"
        return JsonResponse({'result': register_result, 'message': register_message})

    std_img = request.FILES.get('std_img')
    cv2_std_img = cv2.imdecode(np.array(bytearray(std_img.read()), dtype=np.byte), cv2.IMREAD_COLOR)
    try:
        std_feature_vector = FACE_EMBEDDING.get(cv2_std_img)[0].normed_embedding
    except IndexError:
        register_message = "FACE IMAGE ERROR: No face on the picture"
        register_result = "FAILED"
        return JsonResponse({'result': register_result, 'message': register_message})

    stu = Student(std_uid=std_id, std_name=std_name)
    stu_pk_id = stu.id
    data = [{"pk_id": stu_pk_id, "uid": std_id, "vector": std_feature_vector}]
    VECTOR_DB_CLIENT.insert(collection_name=VECTOR_DB_NAME, data=data)
    stu.save()

    register_result = "SUCCESS"
    register_message = "Registered Successfully " + str(stu.std_name) + " " + str(stu.std_uid)

    return JsonResponse({'result': register_result, 'message': register_message})


@api_view(['POST'])
def class_register(request):
    register_result = ""
    register_message = ""

    course_id = int(request.POST.get('courseId'))
    course_name = request.POST.get('courseName')
    course_info = request.POST.get('courseInfo')

    if len(Course.objects.filter(course_id=course_id)) != 0:
        register_result = "FAILED"
        register_message = "Course Already Registered"
        return JsonResponse({'result': register_result, 'message': register_message})

    course = Course(course_id=course_id, course_name=course_name, course_description=course_info)
    course.save()

    register_result = "SUCCESS"
    register_message = "Registered Successfully " + str(course.course_name) + " " + str(course.course_id)
    return JsonResponse({'result': register_result, 'message': register_message})


@api_view(['POST'])
def course_enroll(request):
    register_result = ""
    register_message = ""

    course_id = int(request.POST.get('courseId'))
    student_id = int(request.POST.get('studentId'))
    course_name = request.POST.get('courseName')
    student_name = request.POST.get('studentName')

    if not Course.objects.filter(course_id=course_id).exists():
        register_result = "FAILED"
        register_message = "Course Id Error: this id does not exist"
        return JsonResponse({'result': register_result, 'message': register_message})

    if not Student.objects.filter(std_uid=student_id).exists():
        register_result = "FAILED"
        register_message = "Student Id Error: this id does not exist"
        return JsonResponse({'result': register_result, 'message': register_message})

    if Course.objects.filter(course_id=course_id)[0].course_name != course_name:
        register_result = "FAILED"
        register_message = "Course Name Error: Course Id does not match Course Name"
        return JsonResponse({'result': register_result, 'message': register_message})

    if Student.objects.filter(std_uid=student_id)[0].std_name != student_name:
        register_result = "FAILED"
        register_message = "Student Id Error: Student Id does not match Student Name"
        return JsonResponse({'result': register_result, 'message': register_message})

    stu = Student.objects.get(std_uid=student_id)
    course = Course.objects.get(course_id=course_id)

    if len(Enrollment.objects.filter(Course_Id=course.id, Student_Id=stu.id)) != 0:
        register_result = "FAILED"
        register_message = "This Student Already Enrolled This Course"
        return JsonResponse({'result': register_result, 'message': register_message})

    enrollment = Enrollment(Course_Id=course, Student_Id=stu)
    enrollment.save()

    register_result = "SUCCESS"
    register_message = "Registered Successfully Course: " + str(course_name) + " Student: " + str(student_name)
    return JsonResponse({'result': register_result, 'message': register_message})
