# Generated by Django 4.2.7 on 2024-05-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0020_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
