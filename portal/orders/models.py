from django.db import models
from users.models import MyUser, MarketPlace


# Create your models here.
class StatusOrder(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

class Order(models.Model):
    worker_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    marketplace_id = models.ForeignKey(MarketPlace, on_delete=models.CASCADE)
    order_status_id = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)



class HistoryDescription(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
class OrderHistory(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    history_description_id = models.ForeignKey(HistoryDescription, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, default='')
    date_creation = models.DateTimeField(auto_now_add=True)

class ReworkOrders(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    rework_description = models.CharField(max_length=512)
    # files = models.FileField

class Sizes(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    x_size = models.SmallIntegerField()
    y_size = models.SmallIntegerField()
    z_size = models.SmallIntegerField()
    
class ComplatedAssets(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    complated_files = models.FileField(default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

class SourseAssets(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    sourse_files = models.FileField(upload_to='%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    file_extension = models.CharField(max_length=10, default='')
    size_file = models.IntegerField(default=10)
    # rate_per_face = models.SmallIntegerField()
    # max_val_face = models.SmallIntegerField()
    # num_face = models.SmallIntegerField()

class Tasks(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    # files = models.FileField

class Information(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    ship_by = models.DateField(auto_now_add=True)
    due_by = models.SmallIntegerField()
    font = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    instruction_for_worker = models.TextField()
