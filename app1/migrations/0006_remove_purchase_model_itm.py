# Generated by Django 4.0.5 on 2022-09-08 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_purchase_model_comp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_model',
            name='itm',
        ),
    ]
