from django.db import models


from useful_variables import phone, PARENT_TYPE
from student.models import Student


class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, validators=[phone], default=None)
    student = models.ForeignKey(Student,  null=True, on_delete=models.CASCADE, related_name='parent_student' )
    email = models.CharField(max_length=30)
    cnp = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_cnp', default=None)
    parent_type = models.CharField(max_length=11, choices=PARENT_TYPE)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
