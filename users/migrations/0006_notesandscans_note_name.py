# Generated by Django 2.1.2 on 2019-02-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190226_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesandscans',
            name='note_name',
            field=models.CharField(default='test', max_length=85),
            preserve_default=False,
        ),
    ]
