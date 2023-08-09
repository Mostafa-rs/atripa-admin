from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserUpdateView.as_view()),
    path('users/wallet/<int:pk>/', views.UserWalletRetrieveView.as_view()),
    path('users/finance/<int:pk>/', views.UserFinanceListView.as_view()),
]
