# Generated by Django 2.0 on 2018-11-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shivam_resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdata',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
