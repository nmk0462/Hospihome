# Generated by Django 3.0.8 on 2020-08-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospiHomes', '0023_auto_20200815_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='pic',
            field=models.ImageField(null=True, upload_to='media/gallery'),
        ),
    ]
