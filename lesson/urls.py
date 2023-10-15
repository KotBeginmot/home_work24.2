from django.urls import path

from lesson.apps import LessonConfig
from lesson.views import LessonApiList, LessonApiCreate, LessonApiUpdate, LessonApiRetrieve, LessonApiDelete

app_name = LessonConfig.name

urlpatterns = [
    path('list/', LessonApiList.as_view(), name='lesson_list'),
    path('list/create', LessonApiCreate.as_view(), name='lesson_create'),
    path('list/update/<int:pk>/', LessonApiUpdate.as_view(), name='lesson_update'),
    path('list/detail/<int:pk>/', LessonApiRetrieve.as_view(), name='lesson_detail'),
    path('list/destroy/<int:pk>/', LessonApiDelete.as_view(), name='lesson_destroy'),

]
