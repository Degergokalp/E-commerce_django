# Generated by Django 4.1.2 on 2023-01-04 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0034_cartitems_orderss_remove_orderitems_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='item',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='item',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainClient.items'),
        ),
    ]