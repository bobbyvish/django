# Generated by Django 3.0.2 on 2020-02-18 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mywebsiteapp', '0015_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='active',
        ),
        migrations.AlterField(
            model_name='cart',
            name='Email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Mywebsiteapp.User'),
        ),
    ]
