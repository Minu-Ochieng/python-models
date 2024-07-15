from django.db import models
# Create your models here.

class Student(models.Model):
    # student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    code=models.SmallIntegerField()
    email=models.EmailField()
    # age=models.SmallIntegerField()
    country=models.CharField(max_length=20)
    # phone_number=models.CharField(max_length=20)
    # next_of_kin=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    bio=models.TextField()
    # picture=models.ImageField()
    def __str__(self):
        return f"{self.first_name} {self.first_name}"






# Create your models here.
