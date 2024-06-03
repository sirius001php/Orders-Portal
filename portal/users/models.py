from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    date_registration = models.DateField(auto_now_add=True)
    profile_pic = models.ImageField
    country = models.CharField(max_length=64, default='')
    city = models.CharField(max_length=64, default='')
    mobile = models.CharField(max_length=64, default='')
    

class Worker(models.Model):
    user_id = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    max_val_orders = models.PositiveSmallIntegerField()
    max_val_rework = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user_id.username + ' - Worker'

class Employers(models.Model):
    user_id = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.username + ' - Employer'
class Admin(models.Model):
    user_id = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    comission_per_face = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.user_id.username + ' - Admin'


class RatePerFace(models.Model):
    rate_for_worker = models.DecimalField(max_digits=4, decimal_places=2)
    rate_for_employer = models.DecimalField(max_digits=4, decimal_places=2)
    rate_for_admin = models.DecimalField(max_digits=4, decimal_places=2)

class MarketPlace(models.Model):
    employer_id = models.ForeignKey(Employers, on_delete=models.CASCADE)
    marketplace_name = models.CharField(max_length=64, default='')
    rate_id = models.OneToOneField(RatePerFace, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.marketplace_name



