# Generated by Django 4.1.2 on 2022-11-01 12:22

import MainClient.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('customer_id', models.IntegerField(verbose_name=MainClient.models.Id_generator)),
            ],
        ),
    ]
