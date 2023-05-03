# Generated by Django 4.1.2 on 2023-01-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0030_remove_orderitems_item_orderitems_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='item',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='item',
            field=models.ManyToManyField(to='MainClient.items'),
        ),
    ]