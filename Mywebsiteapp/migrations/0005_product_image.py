# Generated by Django 3.0.2 on 2020-02-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mywebsiteapp', '0004_auto_20200127_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(default='', upload_to='media/image/'),
        ),
    ]
