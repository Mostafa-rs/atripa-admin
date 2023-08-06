from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SupportListCreateView.as_view()),
    path('<int:pk>/', views.SupportRetrieveUpdateDestroyView.as_view()),
    path('chatResponse/<int:pk>/', views.SupportAdminChatCreateView.as_view()),
    path('chats/<int:pk>/', views.SupportChatsListView.as_view()),
    path('adminAssign/<int:pk>/', views.SupportAssignToAdminView.as_view()),
    path('closeSupport/<int:pk>/', views.SupportCloseView.as_view()),
]
