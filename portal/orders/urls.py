from django.urls import path
from orders.views import order, order_create


app_name = 'orders'

urlpatterns = [
   
    path("create/", order_create, name='ordercreate'),
    path("view/<int:order_id>", order, name='order'),
   
] 




