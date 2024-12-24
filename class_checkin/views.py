import os.path

from django.shortcuts import render
from pymilvus import MilvusClient

from class_checkin.models import Student, Enrollment, Course
from djangoProject import settings
# from class_checkin.apps import client
from insightface.app import FaceAnalysis
import cv2
import numpy as np
from djangoProject.settings import VECTOR_DB_NAME

client = MilvusClient(uri="http://localhost:19530", token="root:Milvus")

face_embedding = FaceAnalysis(name='buffalo_l', providers=['CUDAExecutionProvider'])
face_embedding.prepare(ctx_id=0, det_size=(640, 640))


def index(request):
    return render(request, 'checkin/index.html', locals())


def register(request):
    fig = request.FILES.get('personal_fig')
    std_uid = request.FILES.get('uid')
    std_name = request.FILES.get('name')

    cv2_fig = cv2.imdecode(np.array(bytearray(fig.read()), dtype=np.byte), cv2.IMREAD_COLOR)
    feature_vec = face_embedding.get(cv2_fig)[0].embedding_norm
    data = [
        {
            "id": std_uid,
            "uid": std_uid,
            "vector": feature_vec,
        }
    ]
    insert_res = client.insert(collection_name=VECTOR_DB_NAME, data=data)

    return render(request, 'checkin/register.html', locals())

def register_success(request):
    return render(request, 'checkin/register_success.html', {})

def register_fail(request):
    return render(request, 'checkin/register_fail.html', {})

def result(request):
    # get basic variables
    binary_fig = request.FILES.get('checkin_fig')
    # bytearray(binary_fig.chunks())
    course_id = request.POST.get('course_id')
    id = int(course_id)
    course_name = request.POST.get('course_name')

    # course = Course.objects.get(course_id=course_id)
    # assert course.name == course_name

    # get list of student of `course_id`
    query_res = Enrollment.objects.filter(Course_Id=course_id)
    student_uid_set = set([item.Student_Id.std_uid for item in query_res])

    # get list of student attendance today's class

    # convert binary img to rgb metrix
    cv2_fig = cv2.imdecode(np.array(bytearray(binary_fig.read()), dtype=np.byte), cv2.IMREAD_COLOR)

    # get face_embeddings of attendant students
    feature_vec = [face.normed_embedding for face in face_embedding.get(cv2_fig)]

    # search who faces are
    res = client.search(
        collection_name=VECTOR_DB_NAME,
        data=feature_vec,
        limit=1,
        output_fields=["uid", "pk_id"]
    )

    # get students' uid
    attendance_uid_set = set([i[0]['entity']['uid'] for i in res if i[0]['distance'] > 0.9])

    absent_uid_set = student_uid_set.difference(attendance_uid_set)
    unknown_uid_set = attendance_uid_set.difference(student_uid_set)

    absence_mem_list = [Student.objects.filter(std_uid=i)[0] for i in absent_uid_set]
    try:
        substitute_mem_list = [Student.objects.filter(std_uid=i)[0] for i in unknown_uid_set]
    except IndexError:
        substitute_mem_list = []

    attendance_num = len(attendance_uid_set) - len(unknown_uid_set)
    other_listener = len(unknown_uid_set) if len(absent_uid_set) == 0 else 0

    context = {
        'absence_mem_list': absence_mem_list,
        'substitute_mem_list': substitute_mem_list,
        'class_size': len(student_uid_set),
        'attendance_num': attendance_num,  # attendance mem include others
        'absence_num': len(absent_uid_set),
        'other_listener': other_listener,
    }
    return render(request, 'checkin/result.html', context)
