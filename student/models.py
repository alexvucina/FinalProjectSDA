from django.core.exceptions import ValidationError
from django.db import models

from parent.models import Parent

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

ENROLLMENT_CHOICES = [
    ('Preparatory class', 'Preparatory class'),
    ('1st grade', '1st grade'),
    ('2nd grade', '2nd grade'),
    ('3rd grade', '3rd grade'),
    ('4th grade', '4th grade'),
    ('5th grade', '5th grade'),
    ('6th grade', '6th grade'),
    ('7th grade', '7th grade'),
    ('8th grade', '8th grade'),
]

STATUS = [('Active', 'Active'), ('Inactive', 'Inactive')]


def cnp(value):
    if not value.isdigit() or not len(str(value)) == 13:
        raise ValidationError('CNP must contain only numbers of minimum length of 13')


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=8, choices=STATUS, null=False, default='Active')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    CNP = models.CharField(max_length=13, validators=[cnp])
    enrollment = models.CharField(max_length=17, choices=ENROLLMENT_CHOICES)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
