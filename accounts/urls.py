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
    path('admins/', views.AdminsListView.as_view()),
    # Personal info
    path('<int:pk>/', views.UserUpdateView.as_view()),
    # Financial info
    path('wallet/<int:pk>/', views.UserWalletRetrieveView.as_view()),
    path('transactions/<int:pk>/', views.UserFinanceListView.as_view()),
    path('bankAccounts/<int:pk>/', views.UserBankAccountsListView.as_view()),
    # Favorites
    path('favorites/<int:pk>/', views.UserFavoriteRetrieveView.as_view()),
    # Settings
    path('settings/<int:pk>/', views.UserSettingsRetrieveView.as_view()),
    # User's Supports
    path('supports/<int:pk>/', views.UserSupportsListView.as_view()),
    # Supports
    path('supports/list/', views.SupportListView.as_view()),
    path('supports/chats/<int:pk>/', views.UserSupportChatListView.as_view()),
    path('supports/accept/<int:pk>/', views.AdminSupportAccept.as_view()),
    path('supports/closeSupport/<int:pk>/', views.SupportCloseChatView.as_view()),
    path('supports/chatResponse/<int:pk>/', views.SupportChatResponseView.as_view()),
    path('supports/reAssign/<int:pk>/', views.ReassignSupportAdmin.as_view()),
    # Agencies
    path('agencies/', views.AgencyListView.as_view()),
    path('agencies/notDeterminedCount/', views.NotDeterminedAgenciesCountView.as_view()),
]

urlpatterns = [
    path('users/', include(users_paths)),
]
