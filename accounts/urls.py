"""
مسیرهای دسترسی اپلیکیشن کاربران
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""


from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserListCreateView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view()),
]