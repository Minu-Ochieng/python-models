from django.db import models

# Create your models here.
class Class(models.Model):
    class_lecture = models.CharField(max_length=20)
    class_capacity = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length=20)
    class_time= models.TimeField()
    class_id = models.PositiveSmallIntegerField()
    









    def __str__(self) :
        return f"{self.class_name} {self.class_lecture}"