from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from teacher.forms import TeacherForm
from teacher.models import Teacher


class TeacherCreateView(CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('homepage')


class TeacherListView(ListView):
    template_name = 'teacher/list_of_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'
    permission_required = 'teacher.view_list_of_teachers'


class TeacherUpdateView(UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.update_teacher'


class TeacherDeleteView(DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.delete_teacher'


class TeacherDetailView(DetailView):
    template_name = 'teacher/details_teacher.html'
    model = Teacher
    permission_required = 'teacher.view_teacher_details'

