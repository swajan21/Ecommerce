# Generated by Django 4.2.7 on 2024-05-25 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0015_information_remove_slider_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='state',
            new_name='district',
        ),
    ]
