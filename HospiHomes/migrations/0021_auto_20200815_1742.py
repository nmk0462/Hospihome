# Generated by Django 3.0.8 on 2020-08-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospiHomes', '0020_auto_20200815_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='pic',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
