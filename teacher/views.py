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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_teachers = Teacher.objects.all()
        data['all_teachers'] = all_teachers

        return data


class TeacherUpdateView(UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('list-of-teachers')


class TeacherDeleteView(DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list-of-teachers')


class TeacherDetailView(DetailView):
    template_name = 'teacher/details_teacher.html'
    model = Teacher

