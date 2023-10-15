from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet

from course.models import Course
from course.serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer





