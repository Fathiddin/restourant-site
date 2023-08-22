# Generated by Django 4.2.2 on 2023-08-13 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='foods-images/'),
            preserve_default=False,
        ),
    ]
