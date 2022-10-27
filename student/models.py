from django.db import models

from parent.models import Parent

GENRE_CHOICES = [(1, 'Male'), (2, 'Female')]
# ENROLLMENT_CHOICES = [
#     (0, 'Preparatory class'),
#     ('1st grade', 'First grade'),
# ]


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES)
    CNP = models.IntegerField()
    # enrollment = models.CharField(max_length=17, choices=ENROLLMENT_CHOICES)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
