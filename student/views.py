from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from student.forms import StudentForm
from student.models import Student


class StudentCreateView(CreateView):
    template_name = 'student/create_student.html'
    model = Student
    # form_class = StudentForm
    success_url = reverse_lazy('create_student')
    permission_required = 'student.add_student'

    def get_context_data(self, **kwargs):
        data = super(StudentCreateView, self).get_context_data(**kwargs)
        students = Student.objects.all()
        data['all_students'] = students

        return data
