from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializer import Student, StudentSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many = True)
        return Response(serializer.data)
# Create your views here.
