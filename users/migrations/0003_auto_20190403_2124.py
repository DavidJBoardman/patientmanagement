# Generated by Django 2.1.2 on 2019-04-03 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190403_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immunisation',
            name='vaccinedatetime',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Vaccine date administered'),
        ),
        migrations.AlterField(
            model_name='immunisation',
            name='vaccinedose',
            field=models.CharField(max_length=256, verbose_name='Vaccine dose (mg)'),
        ),
        migrations.AlterField(
            model_name='injection',
            name='injectiondatetime',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Injection Date Administered'),
        ),
        migrations.AlterField(
            model_name='injection',
            name='injectiondose',
            field=models.CharField(blank=True, max_length=256, verbose_name='Injection Dose (mg)'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='medstartdatetime',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Medication Start Date'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='height',
            field=models.CharField(blank=True, max_length=256, verbose_name='Height (cm)'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='weight',
            field=models.CharField(blank=True, max_length=256, verbose_name='Weight (kg)'),
        ),
    ]
