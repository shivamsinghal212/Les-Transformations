from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(TeacherProfile)
admin.site.register(TeacherEducation)
admin.site.register(TeacherProfessional)
admin.site.register(TeacherCertification)
admin.site.register(TeacherSubjects)


