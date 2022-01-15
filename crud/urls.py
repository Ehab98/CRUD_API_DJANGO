

from django.urls import path
from .import views
urlpatterns = [



    #API for students
    path('api/students/', views.all_stud ,name='All_student'),
    path('api/student/<int:pk>/', views.stud_id ,name='student_num'),
    path('api/studentupdate/<int:pk>', views.stud_update ,name='student_update'),
    path('api/studentdelete/<int:pk>', views.stud_delete ,name='student_delete'),
    #API for Teachers
    path('api/teachers/', views.all_Teacher ,name='All_Teachers'),
    path('api/teacher/<int:pk>', views.teacher_pk ,name='Teacher_num'),
    #API for Courses
    path('api/courses/', views.all_Courses ,name='All_Courses'),
    path('api/course/<int:pk>', views.course_pk ,name='Course_num'),
    #API for Places
    path('api/Places/', views.all_places ,name='All_Places'),
    path('api/Place/<int:pk>', views.place_pk ,name='Place_num'),
]

