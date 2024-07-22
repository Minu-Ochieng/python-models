from django.db import models
from django.db.models.manager import BaseManager



class Course(models.Model):
    course_id = models.CharField(max_length=100,primary_key=True,default=0)
    course_trainer = models.CharField(max_length=100,blank=True)
    course_objective = models.CharField(max_length=255,blank=True)
    course_duration = models.DurationField(default=0)
    course_description = models.TextField(blank=True)
    pass_mark = models.IntegerField(default=0)
    course_title = models.CharField(max_length=100,blank=True)
    course_teacher = models.CharField(max_length=100,blank=True)
    course_resources = models.CharField(max_length=255,blank=True)
    teaching_assistant = models.CharField(max_length=100,blank=True)
    department = models.CharField(max_length=100,blank=True)

    objects : BaseManager["Course"]




    def __str__(self):
        return f"{self.course_title}"
# Create your models here.