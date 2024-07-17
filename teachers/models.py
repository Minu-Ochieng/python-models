from django.db import models
from django.db.models.manager import BaseManager


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(primary_key=True)
    years_of_experience = models.IntegerField()
    place_of_birth = models.CharField(max_length=100)
    salary = models.IntegerField()
    hire_date = models.DateField()
    bio = models.TextField()



    objects : BaseManager["Teacher"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"