from django.db import models
from django.db.models.manager import BaseManager

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    nationality = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10,blank=True)
    email = models.EmailField(unique=True)
    immediate_contact = models.CharField(max_length=100,blank=True) 
    enrollment_date = models.DateField()
    phone_number = models.CharField(max_length=15,default=0)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    courses = models.ManyToManyField('course.Course', related_name='student')
    classes = models.ManyToManyField('class.Class', related_name='student')
    

    objects : BaseManager["Student"]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"