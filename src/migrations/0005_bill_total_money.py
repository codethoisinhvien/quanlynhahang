# Generated by Django 2.2.11 on 2020-06-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20200607_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='total_money',
            field=models.IntegerField(default=0),
        ),
    ]
