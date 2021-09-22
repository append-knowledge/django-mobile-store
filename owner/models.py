from django.db import models
from datetime import timedelta,date



# Create your models here.
class Mobile(models.Model):
    company = models.CharField(max_length=100)
    model_name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    available_pieces = models.IntegerField()
    image=models.ImageField(upload_to='image',null=True)
    def __str__(self):
        return self.model_name




class Order(models.Model):
    products = models.ForeignKey(Mobile,on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    option = (('delivered', 'delivered'), ('cancel', 'cancel'), ('intransit', 'intransit'), ('ordered', 'ordered'))
    status = models.CharField(max_length=20, choices=option, default='ordered')
    phone_number = models.CharField(max_length=10)
    ed=date.today()+timedelta(days=5)
    delivery_date = models.DateField(null=True,default=ed)
