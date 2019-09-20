# Generated by Django 2.2.5 on 2019-09-19 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='is_sample',
        ),
        migrations.AddField(
            model_name='sample',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='sample',
            name='img_path',
            field=models.FilePathField(default=''),
        ),
        migrations.AddField(
            model_name='sample',
            name='label',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sample',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='sample',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]