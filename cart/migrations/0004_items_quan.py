# Generated by Django 2.2 on 2021-09-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='quan',
            field=models.IntegerField(default=True),
        ),
    ]
