# Generated by Django 3.1.2 on 2020-10-11 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_changes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changes',
            old_name='note',
            new_name='changed_note',
        ),
    ]
