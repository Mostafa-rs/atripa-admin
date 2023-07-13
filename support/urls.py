from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SupportListCreateView.as_view()),
    path('<int:pk>/', views.SupportRetrieveUpdateDestroyView.as_view()),
]
