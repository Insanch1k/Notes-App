# Generated by Django 3.1.2 on 2020-10-11 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201011_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='changes',
            name='changed_version',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='changes',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='changes',
            name='changed_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.note'),
        ),
    ]
