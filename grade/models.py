from django.db import models

from student.models import Student

LIST_OF_GRADES = [
    ('insufficient', 'insufficient'),
    ('sufficient', 'sufficient'),
    ('good', 'good'),
    ('verygood', 'verygood'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
]

TYPE_OF_ACTIVITY = [
    ('Test paper', 'Test paper'),
    ('Listening', 'Listening'),
]


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    grade = models.CharField(max_length=12, choices=LIST_OF_GRADES)
    type_of_activity = models.CharField(max_length=12, choices=TYPE_OF_ACTIVITY)
    date = models.DateField()
