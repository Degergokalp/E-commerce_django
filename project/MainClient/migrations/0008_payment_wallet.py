# Generated by Django 4.1.2 on 2022-11-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0007_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
            ],
        ),
    ]
