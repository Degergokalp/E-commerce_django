# Generated by Django 4.1.2 on 2023-01-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0028_items_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='items',
            name='deneme',
            field=models.IntegerField(default=2),
        ),
    ]