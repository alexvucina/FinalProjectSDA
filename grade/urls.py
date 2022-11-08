from django.urls import path

from grade import views

urlpatterns = [
    path('add_grade/', views.Teacher)
]