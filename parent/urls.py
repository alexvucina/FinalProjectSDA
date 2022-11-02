from django.urls import path
from parent import views

urlpatterns = [
    path('create_parent/', views.ParentCreateView.as_view(), name='create-parent'),
    path('list_of_parents/', views.ParentsListView.as_view(), name='list-of-parents'),
]