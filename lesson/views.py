from rest_framework import generics
from django.shortcuts import render

from lesson.models import Lesson
from lesson.serializer import LessonSerializer


class LessonApiList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonApiCreate(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonApiUpdate(generics.UpdateAPIView):
    serializer_class = LessonSerializer


class LessonApiRetrieve(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonApiDelete(generics.DestroyAPIView):
    serializer_class = LessonSerializer
