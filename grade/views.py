from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class TeacherAddGrade(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = ''
    model = ''
    form_class = ''
    success_url = ''
    permission_required = ''
