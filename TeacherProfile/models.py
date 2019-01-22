from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class TeacherProfile(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)
    language = models.CharField(max_length=20)
    photo = models.URLField
    tid = models.CharField(max_length=6, null=True, blank=True, unique=True)

    def __str__(self):
        return '{}'.format(self.tid)

    def id_generator(self):
        return 'LT{}'.format(len(TeacherProfile.objects.all())+1)

    def save(self,force_insert=False,force_update=False, using=None):
        self.tid = self.id_generator()
        super(TeacherProfile, self).save()


class TeacherEducation(models.Model):

    type = models.CharField(max_length=50, blank=False)
    from_date = models.DateField(editable=True, default=None)
    to_date = models.DateField(editable=True, default=None)
    organisation = models.CharField(max_length=100, default=None)
    description = models.TextField(null=True)
    tid = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, to_field='tid', db_column='tid')

    def __str__(self):
        return '{}-{}'.format(self.tid, self.type)


class TeacherCertification(models.Model):

    valid_date = models.DateField(editable=True, default=None)
    code = models.CharField(max_length=10, blank=True, default=None)
    name = models.CharField(max_length=30, blank=False)
    organisation = models.CharField(max_length=30, blank=False, null=False)
    tid = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, to_field='tid', db_column='tid')

    def __str__(self):
        return '{}-{}'.format(self.tid, self.name)


class TeacherProfessional(models.Model):

    from_date = models.DateField(editable=True, default=None)
    to_date = models.DateField(editable=True, default=None)
    organisation = models.CharField(max_length=30, blank=False, null=False)
    location = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=False, null=False)
    tid = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, to_field='tid', db_column='tid')
    subjects = ArrayField(models.CharField(max_length=200))
    skills = ArrayField(models.CharField(max_length=200, blank=True))
    achievements = models.TextField(null=True)
    recommendations = models.TextField(null=True)

    def __str__(self):
        return '{}-{}'.format(self.tid, self.position)


class TeacherSubjects(models.Model):

    professional_experience = models.ForeignKey(TeacherProfessional, on_delete=models.CASCADE,
                                                related_name='new_subjects')
    code = models.CharField(max_length=5, blank=False, null=False, unique=True)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)

    class Meta:
        unique_together = ('code', 'name')

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)
