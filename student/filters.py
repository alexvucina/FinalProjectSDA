import django_filters
from django import forms
from django.db import models

from django_filters import DateFilter

from student.models import Student, GENDER_CHOICES, STATUS


class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    birthday_start_date_gte = DateFilter(field_name='start_date', label='From birthday start date', lookup_expr='gte',
                                         widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    birthday_end_date_lte = DateFilter(field_name='end_date', label='To birthday end date', lookup_expr='lte',
                                       widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})),
    status = django_filters.CharFilter(choices=STATUS),
    gender = django_filters.ChoiceFilter(choices=GENDER_CHOICES)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a last name'})
        # self.filters['gender'].extra.update(
        #     {'choices': GENDER_CHOICES}
        # )
