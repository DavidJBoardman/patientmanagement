# Generated by Django 2.1.2 on 2019-03-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20190322_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialdetails',
            name='handicaps',
        ),
        migrations.AddField(
            model_name='socialdetails',
            name='disability',
            field=models.CharField(blank=True, max_length=256, verbose_name='disabilities'),
        ),
        migrations.AlterField(
            model_name='socialdetails',
            name='sexualorientation',
            field=models.CharField(blank=True, choices=[('Hetrosexual', 'Hetrosexual'), ('Homosexual', 'Homosexual'), ('Bisexual', 'Bisexual'), ('Prefer not to say', 'Prefer not to say')], max_length=11, verbose_name='Sexual Orientation'),
        ),
    ]