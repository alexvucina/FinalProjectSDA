from django import forms
from django.forms import TextInput, EmailInput, DateInput, Select

from teacher.models import Teacher, Grade
from useful_variables import LIST_OF_GRADES, TYPE_OF_ACTIVITY


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Please enter your address', 'class': 'form-control'}),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['teacher', 'grade', 'type_of_activity', 'date']
        widgets = {
            'teacher': Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(choices=LIST_OF_GRADES, attrs={'class': 'form-control'}),
            'type_of_activity': forms.Select(choices=TYPE_OF_ACTIVITY, attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

