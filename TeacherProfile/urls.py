from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/teacher/profile', TeacherProfileList.as_view()),
    path('api/v1/teacher/profile/<str:tid>', TeacherProfileList.as_view()),
    path('api/v1/teacher/education/<str:tid>', TeacherEducationList.as_view()),
    path('api/v1/teacher/professional/<str:tid>', TeacherProfessionalList.as_view())
]