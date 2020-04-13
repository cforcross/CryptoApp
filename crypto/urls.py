from django.urls import path
from .views import index, prices

urlpatterns = [
    path('', index, name='home'),
    path('prices/', prices, name='prices')
]
