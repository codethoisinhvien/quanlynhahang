import json
import sys

from django.db import migrations

from src.models import FoodGroup, Food, TableGroup, Table, Office

sys.getfilesystemencoding()


def fake_food_group(apps, schema_editor):
    # pass
    data = []
    with open('src/fake_data/food_group.json') as f:
        foods = json.load(f)
        for item in foods:
            food_group = FoodGroup(name=item['name'])
            data.append(food_group)
    FoodGroup.objects.bulk_create(data)


def fake_food(apps, schema_editor):
    data = []
    with open('src/fake_data/food.json') as f:
        foods = json.load(f)
        for item in foods:
            print(item)
            food_group = FoodGroup.objects.get(name=item['food_group'])
            print(food_group)
            food = Food(name=item['name'], price=item['price '], img=item['img '], food_group=food_group)
            data.append(food)
    Food.objects.bulk_create(data)


def fake_office(apps, schema_editor):
    data = []
    with open('src/fake_data/office.json') as f:
        offices = json.load(f)
        for item in offices:
            print(item)
            food = Office(name=item['name'])
            data.append(food)
    Office.objects.bulk_create(data)


def fake_table(apps, schema_editor):
    data = []
    with open('src/fake_data/table.json') as f:
        foods = json.load(f)
        for item in foods:
            print(item)
            table_group = TableGroup.objects.get(name=item['table_group'])

            food = Table(name=item['name'], table_group=table_group, status=item['status'])
            data.append(food)
    Table.objects.bulk_create(data)


def fake_group_table(apps, schema_editor):
    data = []
    with open('src/fake_data/table_group.json') as f:
        foods = json.load(f)
        for item in foods:
            print(item)
            table = TableGroup(name=item['name'])
            data.append(table)
    TableGroup.objects.bulk_create(data)


class Migration(migrations.Migration):
    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fake_food_group),
        migrations.RunPython(fake_food),
        migrations.RunPython(fake_group_table),
        migrations.RunPython(fake_table),
        migrations.RunPython(fake_office)
    ]
