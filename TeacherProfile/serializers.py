from .models import *

from rest_framework import serializers
from .util_serializers import StringArrayField


class TeacherEducationSerializer(serializers.ModelSerializer):

    # teacher_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # tid = serializers.ReadOnlyField()
    class Meta:
        model = TeacherEducation
        fields = ('type', 'from_date', 'to_date', 'organisation', 'description', 'tid',)


class TeacherProfileSerializer(serializers.ModelSerializer):

    # education = TeacherEducationSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherProfile
        fields = ('name', 'email', 'phone', 'language',)


class TeacherProfessionalSerializer(serializers.ModelSerializer):

    # subjects = serializers.StringRelatedField(many=True, read_only=False)
    subjects = StringArrayField()
    skills = StringArrayField()

    class Meta:
        model = TeacherProfessional
        fields = ('from_date', 'to_date', 'organisation',
                  'location', 'position', 'tid', 'subjects',
                  'skills', 'achievements', 'recommendations')


