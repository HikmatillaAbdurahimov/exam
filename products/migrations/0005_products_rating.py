# Generated by Django 5.0.7 on 2024-07-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
