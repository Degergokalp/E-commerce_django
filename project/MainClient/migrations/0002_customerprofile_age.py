# Generated by Django 4.1.2 on 2022-11-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainClient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
