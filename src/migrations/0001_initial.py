# Generated by Django 2.2.11 on 2020-05-11 16:44
import sys

from django.db import migrations, models
import django.db.models.deletion

sys.getfilesystemencoding()
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PA', 'Paid'), ('PE', 'Pending'), ('NP', 'Not Paid')], default='NP', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TableGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('table_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.TableGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('img', models.TextField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fvi.pngtree.com%2Ffree-png-vectors%2Fm%25C3%25B3n-%25C4%2583n&psig=AOvVaw0bAlpC0_s9Ekaf32NarY64&ust=1588576140818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLivwbaRl-kCFQAAAAAdAAAAABAD')),
                ('status', models.BooleanField(default=True)),
                ('food_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.FoodGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Emloyee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Office')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('amount_complete', models.IntegerField(default=0)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_detail', to='src.Bill')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_name', to='src.Food')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Customer'),
        ),
        migrations.AddField(
            model_name='bill',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Table'),
        ),
    ]
