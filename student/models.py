from django.core.exceptions import ValidationError
from django.db import models

from parent.models import Parent

GENDER_CHOICES = [('0', 'Male'), ('1', 'Female')]

ENROLLMENT_CHOICES = [
    ('0', 'Preparatory class'),
    ('1', '1st grade'),
    ('2', '2nd grade'),
    ('3', '3rd grade'),
    ('4', '4th grade'),
    ('5', '5th grade'),
    ('6', '6th grade'),
    ('7', '7th grade'),
    ('8', '8th grade'),

]


def cnp(value):
    if not value.isdigit() or not len(str(value))==13:
        raise ValidationError('CNP must contain only numbers of minimum length of 13')


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    CNP = models.CharField(max_length=13, validators=[cnp])
    enrollment = models.CharField(max_length=17, choices=ENROLLMENT_CHOICES)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
