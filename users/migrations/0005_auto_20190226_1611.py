# Generated by Django 2.1.2 on 2019-02-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190226_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesandscans',
            name='notes',
            field=models.ImageField(upload_to='note_pics'),
        ),
    ]