# Generated by Django 4.1.2 on 2022-11-05 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0003_names_remove_customerprofile_customer_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='names',
        ),
    ]