# Generated by Django 3.0.3 on 2020-03-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0002_auto_20200308_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(default=' ', upload_to='database/image'),
        ),
    ]
