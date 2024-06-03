from django.urls import path
from users.views import login_view, profile, register, logout_view, marketplace_create, marketplace

app_name = 'users'

urlpatterns = [
    path("registr/", register, name='registr',),
    path("login/", login_view, name='login_view',),
    path("profile/", profile, name='profile', ),
    path("logout/", logout_view, name='logout_view',),
    path("marketplace/create", marketplace_create, name='marketplacecreate',),
    path("marketplace/", marketplace, name='marketplace',),
]
