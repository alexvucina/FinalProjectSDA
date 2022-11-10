from django import forms
from django.forms import TextInput, EmailInput, Select

from parent.models import Parent


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent

        fields = ['first_name', 'last_name', 'student', 'phone_number', 'email', 'cnp', 'parent_type']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'cnp': TextInput(attrs={'placeholder': 'Please enter the student\'s CNP', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'parent_type': forms.Select(attrs={'class': 'form-control'})
        }
