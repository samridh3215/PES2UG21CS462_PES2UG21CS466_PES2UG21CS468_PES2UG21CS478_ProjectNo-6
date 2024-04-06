from django.db import models


# Create your models here.

class Item(models.Model):
    name= models.CharField(max_length=200)
    item_id= models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name


# class AddItem(models.Model):
#     itemid= models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity= models.IntegerField()

