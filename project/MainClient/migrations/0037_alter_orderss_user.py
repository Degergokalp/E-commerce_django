# Generated by Django 4.1.2 on 2023-01-04 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainClient', '0036_alter_cartitems_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderss',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
