# Generated by Django 3.1.2 on 2020-10-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201011_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changes',
            name='changed_version',
            field=models.FloatField(),
        ),
    ]
