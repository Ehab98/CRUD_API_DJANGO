from django.contrib import admin
from .models import student,place,Teacher,course
# Register your models here.

admin.site.register(student)

admin.site.register(place)

admin.site.register(Teacher)

admin.site.register(course)
