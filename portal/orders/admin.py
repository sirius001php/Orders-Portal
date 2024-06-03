from django.contrib import admin

from orders.models import Order, StatusOrder, HistoryDescription, OrderHistory, ReworkOrders, Sizes, ComplatedAssets, SourseAssets, Tasks, Information

admin.site.register(Order)
admin.site.register(StatusOrder)
admin.site.register(HistoryDescription)
admin.site.register(ReworkOrders)
admin.site.register(Sizes)
admin.site.register(OrderHistory)
admin.site.register(ComplatedAssets)
admin.site.register(SourseAssets)
admin.site.register(Tasks)
admin.site.register(Information)