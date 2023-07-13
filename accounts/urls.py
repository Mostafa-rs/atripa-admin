from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserListCreateView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view()),
]