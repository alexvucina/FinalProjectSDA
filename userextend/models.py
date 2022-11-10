from django.contrib.auth.models import User
from django.db import models

from useful_variables import ACCOUNT_TYPE


class UserExtend(User):
    gender_options = (('male', 'Male'), ('female', 'Female'))
    date_of_birth = models.DateField()
    gender = models.CharField(choices=gender_options, max_length=6)
    phone = models.CharField(max_length=10)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=7, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'