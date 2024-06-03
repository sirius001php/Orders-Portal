from django.contrib import admin

from django.contrib import admin
from users.models import MyUser, Worker, Employers, RatePerFace, Admin, MarketPlace

admin.site.register(MyUser)
admin.site.register(Worker)
admin.site.register(Employers)
admin.site.register(RatePerFace)
admin.site.register(Admin)
admin.site.register(MarketPlace)