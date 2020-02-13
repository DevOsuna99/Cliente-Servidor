# Generated by Django 3.0.3 on 2020-02-13 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('apellidoPaterno', models.CharField(max_length=254)),
                ('apellidoMaterno', models.CharField(max_length=254)),
                ('edad', models.IntegerField()),
                ('ciudad', models.CharField(max_length=254)),
                ('genero', models.CharField(max_length=254)),
                ('ocupacion', models.CharField(max_length=254)),
                ('estado', models.CharField(max_length=254)),
                ('estadoCivil', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
