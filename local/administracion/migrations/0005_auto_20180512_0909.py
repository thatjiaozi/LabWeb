# Generated by Django 2.0.2 on 2018-05-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_remove_folio_ticketfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteDeVentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
