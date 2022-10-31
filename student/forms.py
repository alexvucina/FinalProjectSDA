from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, DateInput, ChoiceField

from student.models import Student, GENRE_CHOICES, ENROLLMENT_CHOICES


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['first_name', 'last_name', 'date_of_birth', 'genre', 'CNP', 'enrollment']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genre': forms.Select(choices=GENRE_CHOICES, attrs={'class': 'form-control'}),
            'CNP': TextInput(attrs={'placeholder': 'Please enter your CNP', 'class': 'form-control'}),
            'enrollment': forms.Select(choices=ENROLLMENT_CHOICES, attrs={'class': 'form-control'})
        }