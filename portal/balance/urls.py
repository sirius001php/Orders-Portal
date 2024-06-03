from django.urls import path
from balance.views import balance

app_name = 'balance'

urlpatterns = [
    path("", balance, name='balance'),
    
]
