from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherCreateView(CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('homepage')
