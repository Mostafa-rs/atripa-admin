from django.urls import path
from . import views


urlpatterns = [
    path('rewards/', views.RewardListCreateView.as_view())
]
