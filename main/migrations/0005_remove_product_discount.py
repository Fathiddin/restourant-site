# Generated by Django 4.2.2 on 2023-08-15 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_food_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]
