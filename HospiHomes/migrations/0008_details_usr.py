# Generated by Django 3.0.8 on 2020-08-12 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HospiHomes', '0007_upd'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='usr',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
    ]