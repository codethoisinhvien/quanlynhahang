from django.db import models


# Create your models here.
class FoodGroup(models.Model):
    name = models.CharField(max_length=50,unique=True)


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    food_group = models.ForeignKey(FoodGroup,models.CASCADE)
class TableGroup(models.Model):
    name=models.CharField(max_length=50,unique=True)
    price = models.IntegerField(default=0)


# class Table(models.Model):
#     name = models.CharField(max_length=50),

