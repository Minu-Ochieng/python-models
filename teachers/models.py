from django.db import models

# Create your models here.
class Teachers(models.Model):
    teacher_name = models.CharField(max_length=20)
    teacher_id = models.IntegerField()
    teacher_course = models.CharField(max_length=20)
    teacher_class = models.CharField(max_length=20)
    teacher_occupation = models.CharField(max_length=20)
    teacher_description= models.TextField()



    def __str__(self) :
        return f"{self.teacher_name} {self.teacher_course}"