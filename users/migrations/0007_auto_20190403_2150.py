# Generated by Django 2.1.2 on 2019-04-03 20:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190403_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
