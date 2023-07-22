"""
مسیرهای دسترسی اپلیکیشن اطلاعات پایه
برنامه نویس: مصطفی رسولی
mostafarasooli54@gmail.com
1402/04/22
"""

from django.urls import path
from . import views

urlpatterns = [
    path('continentals/', views.ContinentalListView.as_view()),
    path('prefixnumbers/', views.PrefixNumberListView.as_view()),
    path('countries/', views.CountryListCreateView.as_view()),
    path('countries/<int:pk>/', views.CountryRetrieveUpdateDestroyView.as_view()),
    path('provinces/', views.ProvinceListCreateView.as_view()),
    path('provinces/<int:pk>/', views.ProvinceRetrieveUpdateDestroyView.as_view()),
    path('cities/', views.CityListCreateView.as_view()),
    path('cities/<int:pk>/', views.CityRetrieveUpdateDestroyView.as_view()),
    path('terminals/', views.TerminalListCreateView.as_view()),
    path('terminals/<int:pk>/', views.TerminalRetrieveUpdateDestroyView.as_view()),
    path('vehicles/', views.VehicleListCreateView.as_view()),
    path('vehicles/<int:pk>/', views.VehicleRetrieveUpdateDestroyView.as_view()),
    path('accommodations/', views.AccommodationListCreateView.as_view()),
    path('accommodations/<int:pk>/', views.AccommodationRetrieveUpdateDestroyView.as_view()),
    path('banks/', views.BankListCreateView.as_view()),
    path('banks/<int:pk>/', views.BankRetrieveUpdateDestroyView.as_view()),
    path('subscribes/', views.SubscribeListCreateView.as_view()),
    path('subscribes/<int:pk>/', views.SubscribeRetrieveUpdateDestroyView.as_view()),
    path('supports/', views.SupportListCreateView.as_view()),
    path('supports/<int:pk>/', views.SupportRetrieveUpdateDestroyView.as_view()),
    path('companies/', views.CompanyListCreateView.as_view()),
    path('companies/<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view()),
]
