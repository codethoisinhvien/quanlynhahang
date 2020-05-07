import json

from django.db import migrations

from src.models import FoodGroup, Food


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
            food = Food(name=item['name'],price=item['price '],food_group=food_group)
            data.append(food)
    Food.objects.bulk_create(data)


class Migration(migrations.Migration):
    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fake_food_group),
        migrations.RunPython(fake_food)
    ]
