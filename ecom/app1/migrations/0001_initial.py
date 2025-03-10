# Generated by Django 5.1.4 on 2025-01-14 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('image', models.FileField(upload_to='file')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passw', models.CharField(max_length=100)),
                ('utype', models.CharField(max_length=50)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.reg_form')),
            ],
        ),
    ]
