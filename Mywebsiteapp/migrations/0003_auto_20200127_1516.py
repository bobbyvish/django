# Generated by Django 3.0.2 on 2020-01-27 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mywebsiteapp', '0002_auto_20200127_1515'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
