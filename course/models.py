from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_code = models.PositiveSmallIntegerField()
    course_instructor = models.CharField(max_length=20)
    course_assigment= models.CharField(max_length=20)
    course_level = models.IntegerField()
    





    def __str__(self) :
        return f"{self.course_instructor} {self.course_name}"