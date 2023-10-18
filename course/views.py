from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response, viewsets
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.filters import OrderingFilter
from course.models import Course, Payments
from course.serializer import CourseSerializer, PaymentsSerializer, CourseCreateSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        'create': CourseCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'payment_method')
    ordering_field = ('payment_date',)
