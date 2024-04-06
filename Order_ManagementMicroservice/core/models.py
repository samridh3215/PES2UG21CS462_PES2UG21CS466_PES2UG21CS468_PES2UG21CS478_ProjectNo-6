from django.db import models

# Create your models here.
# class Item(models.Model):
#     name= models.CharField(max_length=200)
#     item_id= models.IntegerField()
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     def __str__(self):
#         return self.name

class CartItem(models.Model):
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.name} (${self.price})"