# Generated by Django 2.1.1 on 2020-01-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200120_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='products/%Y/%m/%d/'),
        ),
    ]
