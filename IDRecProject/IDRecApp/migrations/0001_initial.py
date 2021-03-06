# Generated by Django 3.1.5 on 2021-01-16 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=100)),
                ('forenames', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(max_length=100)),
                ('country_of_birth', models.CharField(max_length=100)),
                ('date_issued', models.CharField(max_length=100)),
                ('id_no', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepaths', models.FileField(max_length=200, upload_to='uploaded')),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
    ]
