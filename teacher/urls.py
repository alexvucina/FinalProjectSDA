from django.urls import path

from teacher import views

urlpatterns = [
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create-teacher'),
    path('list_of_teachers/', views.TeacherListView.as_view(), name='list-of-teachers'),
    path('update_teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='update-teacher'),
    path('delete_teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete-teacher'),
    path('details_teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='details-teacher'),
    path('add_grade/', views.TeacherAddGrade.as_view(), name='add-grade'),
]
