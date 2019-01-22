from .models import TeacherProfile as Tp


def get_teacher_object_length(tid):
    teacher_object = Tp.objects.filter(tid=tid)
    return len(teacher_object)