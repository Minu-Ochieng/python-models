from django.db import models
from student.models import Student
# Create your models here.
class Class(models.Model):
    class_rules=models.TextField(max_length=20)
    class_capacity=models.SmallIntegerField()
    class_performance=models.CharField(max_length=30)
    class_lecture=models.CharField(max_length=30)
    class_id=models.SmallIntegerField()
    class_name=models.CharField(max_length=30)
    class_representative=models.CharField(max_length=30)
    class_description=models.TextField(max_length=30)
    class_table_number=models.SmallIntegerField()
    class_bio=models.CharField(max_length=30)
    class_rules=models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.class_bio} {self.class_description}"