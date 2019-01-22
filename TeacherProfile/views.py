from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

from .models import TeacherProfile as Tp
from .models import TeacherEducation as Te
from .models import TeacherProfessional as Tpf

from .utils_api import get_teacher_object_length
from django.core.exceptions import ObjectDoesNotExist


from django.http import Http404


# Create your views here.


class TeacherProfileList(APIView):

    @staticmethod
    def get(request, tid):

        """
        :param request: /api/v1/teacher/profile/{}
        :param tid: LT1
        :return: {
                "name": "shivam singhal",
                "email": "Shivam.singhal212@gmail.com",
                "phone": 9503182221,
                "language": "India",
                "tid": "LT1"
            }
        """

        if get_teacher_object_length(tid) == 0:
            return Response({'error': 'Invalid TID.'})
        else:
            profile_objects = Tp.objects.filter(tid=tid).values('name', 'email', 'phone', 'language', 'tid')
        if profile_objects:
            return Response(profile_objects[0])
        else:
            return Response({'error': 'Invalid TID.'})

    @staticmethod
    def post(request):
        serializer = TeacherProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            registered_tid = Tp.objects.filter(email=serializer.data['email']).values('tid')[0]['tid']
            return Response({'api_success': True, 'tid': registered_tid}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherEducationList(APIView):

    @staticmethod
    def get(tid):
        if get_teacher_object_length(tid) == 0:
            return Response({'error': 'Invalid TID.'})
        else:
            education_objects = Te.objects.filter(tid=tid).values('type', 'tid', 'from_date', 'to_date', 'organisation',
                                                                  'description')
        serializer = TeacherEducationSerializer(data=list(education_objects), many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    @staticmethod
    def post(request, tid):
        request_data = request.data.copy()
        if get_teacher_object_length(tid) == 0:
            return Response({'error': 'Invalid TID.'})
        else:
            request_data['tid'] = tid
        serializer = TeacherEducationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'api_success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, tid):
        if get_teacher_object_length(tid) == 0:
            return Response({'error': 'Invalid TID.'})
        else:

            request_data = request.data.copy()

        if 'type' not in request_data:
            return Response({'error': '"type" missing in request'},status=status.HTTP_400_BAD_REQUEST)
        else:
            deleted_data = Te.objects.filter(tid=tid,type=request_data['type']).delete()[0]
            return Response({'message': str(deleted_data) + ' records deleted.'}, status=status.HTTP_200_OK)


class TeacherProfessionalList(APIView):

    def get(self, request, tid):
        if get_teacher_object_length(tid) == 0:
            return Response({'error': 'Invalid TID.'})
        else:
            professional_objects = Tpf.objects.filter(tid=tid).values('from_date', 'to_date', 'organisation',
                                                                      'location', 'position', 'tid', 'subjects',
                                                                      'skills', 'achievements', 'recommendations')
        serializer = TeacherProfessionalSerializer(data=list(professional_objects), many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def post(self, request, tid):
        request_data = request.data.copy()
        print('request_data', request_data)
        if get_teacher_object_length(tid) == 0:
            return Response({'error': 'Invalid TID.'})
        else:
            request_data['tid'] = tid
        serializer = TeacherProfessionalSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'api_success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




