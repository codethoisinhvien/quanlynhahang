from django.db import models


# Create your models here.
class FoodGroup(models.Model):
    name = models.CharField(max_length=50)


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.BooleanField()
    food_group = models.ForeignKey(FoodGroup,models.CASCADE)

