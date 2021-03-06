from django.db import models


# Create your models here.
class FoodGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.TextField(
        default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fvi.pngtree.com%2Ffree-png-vectors%2Fm%25C3%25B3n-%25C4%2583n&psig=AOvVaw0bAlpC0_s9Ekaf32NarY64&ust=1588576140818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLivwbaRl-kCFQAAAAAdAAAAABAD")
    status = models.BooleanField(default=True)
    food_group = models.ForeignKey(FoodGroup, models.CASCADE)


class TableGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(default=0)


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(default=0),
    table_group = models.ForeignKey(TableGroup, models.CASCADE)
    # slot_amount = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=True)


class Office(models.Model):
    name = models.CharField(max_length=50, unique=True)


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    office = models.ForeignKey(Office, models.CASCADE)


class Emloyee(models.Model):
    full_name = models.CharField(max_length=100)
    office = models.ForeignKey(Office, models.CASCADE)


class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bill(TimeStampMixin):
    table = models.ForeignKey(Table, models.CASCADE)
    customer = models.ForeignKey(Customer, models.CASCADE)
    total_money = models.IntegerField(default=0)
    status = models.CharField(max_length=2)


class BillDetail(TimeStampMixin):
    bill = models.ForeignKey(Bill, related_name='bill_detail', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='food_name', on_delete=models.CASCADE)
    amount = models.IntegerField()
    amount_complete = models.IntegerField(default=0)
    status = models.BooleanField(default=True)


class ChefBill(TimeStampMixin):
    bill_detail = models.ForeignKey(BillDetail, related_name='bill_chef', on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.BooleanField(default=True)
    delivery_by = models.CharField(default="", max_length=50, )


class DeliveryBill(TimeStampMixin):
    table = models.ForeignKey(Table, related_name='bill_detail', on_delete=models.CASCADE)
    create_by = models.CharField(default="", max_length=50, )
