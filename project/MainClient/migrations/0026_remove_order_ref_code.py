# Generated by Django 4.1.2 on 2023-01-03 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0025_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ref_code',
        ),
    ]