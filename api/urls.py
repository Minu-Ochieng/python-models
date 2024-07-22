from  django.urls import path,
from .views import StudentListView
from .views import ClassPeriodListView
from .views import CourseListView
from .views import TeacherListView
from .views import StudentDetailView

urlpatterns =[
    path ('students/',StudentListView.as_view(),name="student_list_view"),
    path ('students/',ClassPeriodListView.as_view(),name="classperiod_list_view"),
    path ('students/',CourseListView.as_view(),name="course_list_view"),
    path ('students/',TeacherListView.as_view(),name="teacher_list_view"),
    path ('students/',StudentDetailView.as_view(),name="studentdetail_list_view"),

]