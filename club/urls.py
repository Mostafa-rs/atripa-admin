from django.urls import path
from . import views


urlpatterns = [
    path('rewards/', views.RewardListCreateView.as_view()),
    path('rewards/<int:pk>/', views.RewardRetrieveUpdateDestroyView.as_view()),
    path('categories/', views.RewardCategoryListCreateView.as_view()),
    path('categories/<int:pk>/', views.RewardCategoryRetrieveUpdateDestroyView.as_view()),
]
