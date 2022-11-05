from django.core.exceptions import ValidationError
from django.db import models

PARENT_TYPE = [('Mother', 'Mother'), ('Father', 'Father'), ('Grandmother', 'Grandmother'),
               ('Grandfather', 'Grandfather')]


def phone(value):
    if not value.isdigit() or not len(str(value)) == 10:
        raise ValidationError('Please enter only digits')


class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, validators=[phone])
    email = models.CharField(max_length=30)
    parent_type = models.CharField(max_length=11, choices=PARENT_TYPE)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
