from datetime import date, datetime
from class_period.models import ClassPeriod
from course.models import Course
from student.models import Student
from rest_framework import serializers
from student.models import Student
from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
    
    class Meta:
        model = Teacher
        fields = ['id', 'full_name','email']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Course
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name','teacher']

class Student_ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Student
        fields = "__all__"
    
class MinimalStudent_ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','capacity']

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many = True)
    class_enrolled = Student_ClassSerializer()
    class Meta:
        model = Student
        fields = "__all__"
        # exclude = ["email"]  
    
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"

    def get_age(self, object):
        if object.date_of_birth:
            today = datetime.now()
        if isinstance(object.date_of_birth, date) and not isinstance(object.date_of_birth, datetime):
            date_of_birth = datetime.combine(object.date_of_birth, datetime.min.time())
        else:
            date_of_birth = object.date_of_birth
        
        age = today - date_of_birth
        return age.days // 365  
    
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age']

class Class_PeriodSerializer(serializers.ModelSerializer):
    student_class = Student_ClassSerializer()
    
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class MinimalClass_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'name', 'start_time', 'end_time']