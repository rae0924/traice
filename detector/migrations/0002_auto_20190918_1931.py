# Generated by Django 2.2.5 on 2019-09-19 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertrial',
            name='detector_prediction',
            field=models.IntegerField(default=0),
        ),
    ]
