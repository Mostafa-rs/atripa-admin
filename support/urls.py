"""
    Support Serializers
    Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/26
"""

from django.urls import path
from . import views

urlpatterns = [
    path('site/contact_form/', views.ContactForm.as_view()),
]
