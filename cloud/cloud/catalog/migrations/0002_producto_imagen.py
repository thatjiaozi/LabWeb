# Generated by Django 2.0.2 on 2018-05-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Imagen',
            field=models.CharField(default='', max_length=300),
        ),
    ]