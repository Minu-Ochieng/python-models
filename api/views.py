from django.shortcuts import render
from api.serializer import Class_PeriodSerializer, CourseSerializer, MinimalClass_PeriodSerializer, MinimalCourseSerializer, MinimalStudent_ClassSerializer, MinimalStudentSerializer, MinimalTeacherSerializer, Student_ClassSerializer, StudentSerializer, TeacherSerializer
from class_period.models import Class_Period
from course.models import Course

from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student

from teachers.models import Teacher
from rest_framework import status

# Create your views here.
class StudentListViews(APIView):
    def get(self, request):
        student = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name: 
            Students = Students.filter(first_name = first_name)
        country = request.query_params.get("country")
        if country:
            Students = Students.filter(country = country)
        serializer = StudentSerializer(student, many=True)
        serializer = MinimalStudentSerializer(student, many = True)
        return Response(serializer.data)
       
    def post(self, request):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def enroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)
    
    def add_to_class(self, student, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.students.add(student)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)  
    
class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        serializer = MinimalTeacherSerializer(teacher, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)

    def assign_class(self, teacher, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        serializer = MinimalCourseSerializer(course, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class Student_ClassListViews(APIView):
    def get(self, request):
        student_class = Student.objects.all()
        serializer = Student_ClassSerializer(student_class, many=True)
        serializer = MinimalStudent_ClassSerializer(student_class, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Student_ClassSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class Student_ClassDetailView(APIView):
    def get(self, request,id):
        student_class = Student.objects.get(id=id)
        serializer = Student_ClassSerializer(student_class)
        return Response(serializer.data)
    
    def put(self, request,id):
        student_class = Student.objects.get(id=id)
        serializer = Student_ClassSerializer(student_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        student_class = Student.objects.get(id=id)
        student_class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class Class_PeriodListViews(APIView):
    def get(self, request):
        classperiod = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(classperiod, many=True)
        serializer = MinimalClass_PeriodSerializer(classperiod, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =Class_PeriodSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class Class_PeriodDetailView(APIView):
    def get(self, request,id):
        classperiod = Class_Period.objects.get(id=id)
        serializer = Class_PeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod= Class_Period.objects.get(id=id)
        serializer = Class_PeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classperiod = Class_Period.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "get_timetable":
            self.get_timetable(id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        class_period = Class_Period(teacher=teacher, course=course)
        class_period.save()
        return Response(status=status.HTTP_201_CREATED)
    
    def get_timetable(self, request, id):
        class_period = Class_Period.objects.get(id=id)
        timetable = []
        for day in range(7):  
            day_timetable = []
            for period in class_period.periods.filter(day=day):
                day_timetable.append({
                    'start_time': period.start_time,
                    'end_time': period.end_time,
                    'course': period.course.name,
                    'teacher': period.teacher.name,
                    'student_class': period.student_class.name
                })
            timetable.append(day_timetable)
        return Response({'timetable': timetable})
