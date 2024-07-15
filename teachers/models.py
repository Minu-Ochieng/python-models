from django.db import models
from student.models import Student

# Create your models here.
class Teacher(models.Model):
    teacher_age=models.SmallIntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.SmallIntegerField()
    teacher_course=models.CharField(max_length=20)
    teacher_contact=models.CharField(max_length=20)
    teacher_description=models.TextField(max_length=20)
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.SmallIntegerField()
    # teacher_headshot=models.ImageField()
    # teacher_bank_account=models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.teacher_description} {self.teacher_age}'