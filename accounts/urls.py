"""
    Account paths
    Author: Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/12
"""

from django.urls import path, include
from . import views


users_paths = [
    # Users list
    path('', views.UserListView.as_view()),
    # Personal info
    path('<int:pk>/', views.UserUpdateView.as_view()),
    # Financial info
    path('wallet/<int:pk>/', views.UserWalletRetrieveView.as_view()),
    path('transactions/<int:pk>/', views.UserFinanceListView.as_view()),
    path('bankAccounts/<int:pk>/', views.UserBankAccountsListView.as_view()),
    # Support
    path('suuports/requests/<int:pk>/', views.UserSupportRequestListView.as_view()),
    path('suuports/chats/<int:pk>/', views.UserSupportChatListView.as_view()),
    # Favorites
    path('favorites/<int:pk>/', views.UserFavoriteRetrieveView.as_view()),
    # Settings
    path('settings/<int:pk>/', views.UserSettingsRetrieveView.as_view())
]

urlpatterns = [
    path('users/', include(users_paths)),
]
