# Generated by Django 2.2 on 2021-09-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_products_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='products',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
