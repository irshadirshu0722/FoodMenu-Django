from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Item(models.Model):
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desp = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://www.yanaya.co.zw/wp-content/uploads/2020/08/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.jpg")
    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})

