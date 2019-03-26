# Generated by Django 2.1.2 on 2019-02-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190226_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialdetails',
            name='drink',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], default='y', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialdetails',
            name='sexuallyactive',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='socialdetails',
            name='smoking',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='socialdetails',
            name='socialdruguse',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10),
        ),
    ]