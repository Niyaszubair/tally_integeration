# Generated by Django 4.0.5 on 2022-09-08 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_creategodown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creategodown',
            name='itm',
        ),
    ]