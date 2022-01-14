from django.db import models

# Create your models here.
class student(models.Model):

    stud_name = models.CharField( max_length=100)
    stud_email = models.EmailField(max_length=254)
    stud_phone = models.CharField(max_length=15)
    course_name =models.ForeignKey("crud.course",on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("student")
        verbose_name_plural = ("students")

    def __str__(self):
        return self.stud_name


class Teacher(models.Model):
    teacher_name = models.CharField( max_length=100)
    teacher_email = models.EmailField(max_length=254)
    teacher_phone=models.CharField(max_length=15)
    teacher_course = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Teacher")
        verbose_name_plural = ("Teachers")

    def __str__(self):
        return self.teacher_name


class place (models.Model):
    place_hall = models.CharField(max_length=50)
    place_floor = models.CharField(max_length=50)
    place_teacher_name =models.ForeignKey("crud.Teacher", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("place")
        verbose_name_plural = ("places")

    def __str__(self):
        return self.place_hall


class course (models.Model):

    course_name = models.CharField(max_length=100)
    course_start =models.DateField()
    course_finish =models.DateField()
    teacher_name =models.ForeignKey("crud.Teacher", on_delete=models.CASCADE)
    place_hall =models.ForeignKey("crud.place", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("course ")
        verbose_name_plural = ("courses")

    def __str__(self):
        return self.course_name


