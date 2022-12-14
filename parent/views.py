from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from parent.forms import ParentForm
from parent.models import Parent


class ParentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'parent/create_parent.html'
    model = Parent
    form_class = ParentForm
    success_url = reverse_lazy('create-parent')
    permission_required = 'parent.add_parent'


class ParentsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'parent/list_of_parents.html'
    model = Parent
    context_object_name = 'all_parents'
    permission_required = 'parent.view_list_of_parents'

    def get_context_data(self, **kwargs):
        data = super(ParentsListView, self).get_context_data(**kwargs)
        parents = Parent.objects.all()
        data['all_parents'] = parents
        return data


class ParentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'parent/update_parent.html'
    model = Parent
    success_url = reverse_lazy('list-of-parents')
    permission_required = 'parent.update_parent'


class ParentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'parent/delete_parent.html'
    model = Parent
    success_url = reverse_lazy('list-of-parents')
    permission_required = 'parent.delete_parent'


class ParentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'parent/details_parent.html'
    model = Parent
    permission_required = 'parent.view_trainer_details'

