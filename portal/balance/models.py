from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import MyUser

# Create your models here.
class Balance(models.Model):
    bal_in_proces = models.DecimalField(max_digits=10, decimal_places=2)
    bal_wait = models.DecimalField(max_digits=10, decimal_places=2)
    bal_complete = models.DecimalField(max_digits=10, decimal_places=2)

    user_id = models.OneToOneField(MyUser, on_delete=models.SET_NULL, null=True)

class StatusTransaction(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Transaction(models.Model):
    balance_id = models.ForeignKey(Balance, on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True)
    modifed_on = models.DateField(auto_now=True)
    status_id = models.ForeignKey(StatusTransaction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
 



# # Створюємо екземпляр балансу при створенні нового користувача
# @receiver(post_save, sender=User)
# def create_balance(sender, instance, created, **kwargs):
#     if created:
#         Balance.objects.create(user=instance)