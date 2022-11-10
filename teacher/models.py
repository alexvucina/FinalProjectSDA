from django.db import models

from useful_variables import phone, LIST_OF_GRADES, TYPE_OF_ACTIVITY


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, default=None)
    phone_number = models.CharField(max_length=10, validators=[phone])
    address = models.CharField(max_length=50, default=None)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Grade(models.Model):
    # student = models.ManyToManyField(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    grade = models.CharField(max_length=12, choices=LIST_OF_GRADES)
    type_of_activity = models.CharField(max_length=12, choices=TYPE_OF_ACTIVITY)
    date = models.DateField()
