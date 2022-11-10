from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from teacher.forms import TeacherForm, GradeForm
from teacher.models import Teacher, Grade


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('homepage')
    permission_required = 'trainer.add_teacher'


class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'teacher/list_of_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'
    permission_required = 'trainer.view_list_of_teachers'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_teachers = Teacher.objects.all()
        data['all_teachers'] = all_teachers

        return data


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('list-of-teachers')
    permission_required = 'trainer.update_teacher'


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list-of-teachers')
    permission_required = 'trainer.delete_teacher'


class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'teacher/details_teacher.html'
    model = Teacher
    permission_required = 'view_teacher_details'


class TeacherAddGrade(LoginRequiredMixin, CreateView):
    template_name = 'teacher/add_grade.html'
    model = Grade
    form_class = GradeForm
    success_url = reverse_lazy('homepage')
    permission_required = ''
