from django.db import models
from authentication.models import User

# Create your models here.
class FoodGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    food_group = models.ForeignKey(FoodGroup, models.CASCADE)


class TableGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(default=0)


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(default=0),
    table_group = models.ForeignKey(TableGroup, models.CASCADE)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=True)


class Office(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Emloyee(models.Model):
    full_name = models.CharField(max_length=100)
    office = models.ForeignKey(Office, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bill(TimeStampMixin):
    Paid = 'PA'
    Pending = 'PE'
    NotPaid = 'NP'
    Nstatus = (
        (Paid, 'Paid'),
        (Pending, 'Pending'),
        (NotPaid, 'Not Paid')

    )
    table = models.ForeignKey(Table, models.CASCADE)
    customer = models.ForeignKey(Customer, models.CASCADE)
    status = models.CharField(choices=Nstatus,max_length=2,default=NotPaid)


class BillDetail(TimeStampMixin):
    bill = models.ForeignKey(Bill, models.CASCADE)
    food = models.ForeignKey(Food, models.CASCADE)
    amount = models.IntegerField()
    amount_complete = models.IntegerField()
