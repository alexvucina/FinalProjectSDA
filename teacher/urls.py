from django.urls import path

from teacher import views

urlpatterns = [
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
]
