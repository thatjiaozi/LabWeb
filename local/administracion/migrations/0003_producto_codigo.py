# Generated by Django 2.0.2 on 2018-03-13 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_auto_20180313_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Codigo',
            field=models.CharField(default='none', max_length=128),
        ),
    ]
