from email import message
from django.shortcuts import render
from .serializers import CourseSerializer, PlaceSerializer, StudentSerializer, TeacherSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import student , place , course , Teacher
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def all_stud(request):

    if request.method == 'GET':
        students = student.objects.all()
        SerializeStudent = StudentSerializer(students,many=True)
        #return Response 
        return Response(SerializeStudent.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        SerializeStudent = StudentSerializer(data=request.data)
        if SerializeStudent.is_valid():
            SerializeStudent.save()
            return Response(SerializeStudent.data,status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def stud_id(request,pk):
    try:
        students = student.objects.get(id=pk)
        SerializeStudent = StudentSerializer(students,many=False)
        return Response(SerializeStudent.data,status=status.HTTP_200_OK)
    #return Response 
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



#Start of student API 
@api_view(['POST'])
def stud_update(request,pk):
    try:
        students = student.objects.get(id=pk)
        SerializeStudent = StudentSerializer(instance=students , data=request.data)
        if SerializeStudent.is_valid():
            SerializeStudent.save()
        return Response(SerializeStudent.data,status=status.HTTP_200_OK,message='Student updated successfully')
    #return Response 
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def stud_delete(request,pk):
    try:
        student_pk = student.objects.get(id=pk)
        student_pk.delete()
        students = student.objects.all()
        SerializeStudent = StudentSerializer(students ,many=True)
        
        return Response(SerializeStudent.data,status=status.HTTP_200_OK,message='Student updated successfully')
    #return Response 
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
#End of student API

#Start of Teachers API 

@api_view(['GET','POST'])
def all_Teacher(request):

    if request.method == 'GET':
        teachers = Teacher.objects.all()
        SerializeTeachers = TeacherSerializer(teachers,many=True)
        #return Response 
        return Response(SerializeTeachers.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        SerializeTeachers = TeacherSerializer(data=request.data)
        if SerializeTeachers.is_valid():
            SerializeTeachers.save()
            return Response(SerializeTeachers.data,status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def teacher_pk(request,pk):
    try:
        teachers = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)    

    #GET
    if request.method == 'GET':
        SerializeTeachers= TeacherSerializer(teachers)
        return Response (SerializeTeachers.data)

    #PUT
    if request.method == 'PUT':
        SerializeTeachers = TeacherSerializer(teachers,data=request.data)
        if SerializeTeachers.is_valid():
            SerializeTeachers.save()
            return Response(SerializeTeachers.data)
        return Response(SerializeTeachers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method == 'DELETE':
        teachers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#End of Teachers API

#Start of Courses API 
@api_view(['GET','POST'])
def all_Courses(request):

    if request.method == 'GET':
        courses = course.objects.all()
        SerializeCourses = CourseSerializer(courses,many=True)
        #return Response 
        return Response(SerializeCourses.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        SerializeCourses = CourseSerializer(data=request.data)
        if SerializeCourses.is_valid():
            SerializeCourses.save()
            return Response(SerializeCourses.data,status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def course_pk(request,pk):
    try:
        courses = course.objects.get(pk=pk)
    except course.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)    

    #GET
    if request.method == 'GET':
        SerializeCourses= CourseSerializer(courses)
        return Response (SerializeCourses.data)

    #PUT
    if request.method == 'PUT':
        SerializeCourses = CourseSerializer(courses,data=request.data)
        if SerializeCourses.is_valid():
            SerializeCourses.save()
            return Response(SerializeCourses.data)
        return Response(SerializeCourses.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method == 'DELETE':
        courses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#End of Courses API


#Start of Places API 

@api_view(['GET','POST'])
def all_places(request):

    if request.method == 'GET':
        places = place.objects.all()
        Serializeplaces = PlaceSerializer(places,many=True)
        #return Response 
        return Response(Serializeplaces.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        Serializeplaces = PlaceSerializer(data=request.data)
        if Serializeplaces.is_valid():
            Serializeplaces.save()
            return Response(Serializeplaces.data,status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def place_pk(request,pk):
    try:
        places = course.objects.get(pk=pk)
    except course.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)    

    #GET
    if request.method == 'GET':
        Serializeplaces= PlaceSerializer(places)
        return Response (Serializeplaces.data)

    #PUT
    if request.method == 'PUT':
        Serializeplaces = PlaceSerializer(places,data=request.data)
        if Serializeplaces.is_valid():
            Serializeplaces.save()
            return Response(Serializeplaces.data)
        return Response(Serializeplaces.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method == 'DELETE':
        places.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#End of places API