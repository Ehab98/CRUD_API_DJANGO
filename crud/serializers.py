from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import student, course, Teacher, place


class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = '__all__'
