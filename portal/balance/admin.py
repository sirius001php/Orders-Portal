from django.contrib import admin

from balance.models import Balance, Transaction, StatusTransaction
# Register your models here.
admin.site.register(Balance)
admin.site.register(Transaction)
admin.site.register(StatusTransaction)