# Generated by Django 2.1.2 on 2019-02-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_notesandscans_note_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardiandetails',
            name='guardianfirstname',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='guardiandetails',
            name='guardianlastname',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='guardiandetails',
            name='guardiantitle',
            field=models.CharField(blank=True, choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.'), ('DR', 'Dr.'), ('SIR', 'Sir.')], max_length=256),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'Other')], max_length=256),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='patienttitle',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.'), ('DR', 'Dr.'), ('SIR', 'Sir.')], max_length=4),
        ),
    ]
