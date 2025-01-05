from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.
def index(request):
    pass


@api_view(['GET'])
def student_register(request):
    pass


def student_register_success(request):
    pass


def student_register_fail(request):
    pass


def class_register(request):
    pass


def class_register_success(request):
    pass


def class_register_fail(request):
    pass


def course_enroll(request):
    pass


def course_enroll_success(request):
    pass


def course_enroll_fail(request):
    pass
