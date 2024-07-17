from django.db import models
from django.db.models.manager import BaseManager



class Course(models.Model):
    course_id = models.CharField(max_length=100,primary_key=True)
    course_trainer = models.CharField(max_length=100)
    course_objective = models.CharField(max_length=255)
    course_duration = models.DurationField()
    course_description = models.TextField()
    pass_mark = models.IntegerField()
    course_title = models.CharField(max_length=100)
    course_teacher = models.CharField(max_length=100)
    course_resources = models.CharField(max_length=255)
    teaching_assistant = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    objects : BaseManager["Course"]




    def __str__(self):
        return f"{self.course_title}"
# Create your models here.