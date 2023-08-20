from django.urls import path, include

order_paths = [

]

urlpatterns = [
    path('orders/', include(order_paths))
]