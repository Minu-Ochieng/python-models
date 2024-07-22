
from django.db import models



class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=50,primary_key=True,blank=True)
    room_allocation = models.CharField(max_length=100)
    no_of_tables = models.PositiveSmallIntegerField(blank=True)
    no_of_students = models.PositiveSmallIntegerField(blank=False)
    class_representative = models.CharField(max_length=10,blank=True)
    class_goals = models.TextField(blank=True)
    class_meeting = models.CharField(max_length=100,blank=True)
    period_entity = models.CharField(max_length=100,blank=True)
    # course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.class_name}"
    
# Create your models here.
