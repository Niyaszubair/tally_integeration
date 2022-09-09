# Generated by Django 4.0.5 on 2022-09-09 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_delete_ledgercreatemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ledgercreatemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=250)),
                ('lalias', models.CharField(max_length=250)),
                ('lunder', models.CharField(max_length=250)),
                ('lmname', models.CharField(max_length=250)),
                ('laddress', models.CharField(max_length=250)),
                ('lstate', models.CharField(max_length=250)),
                ('lcountry', models.CharField(max_length=250)),
                ('lpincode', models.CharField(max_length=250)),
                ('lbank', models.CharField(max_length=250)),
                ('lpan', models.CharField(max_length=250)),
                ('lreg', models.CharField(max_length=250)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
    ]
