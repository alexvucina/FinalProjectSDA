from django.urls import path

from . import views

urlpatterns = [
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
]