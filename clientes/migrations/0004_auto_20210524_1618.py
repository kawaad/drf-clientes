# Generated by Django 3.0.8 on 2021-05-24 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together={('nome', 'rg', 'celular')},
        ),
    ]
