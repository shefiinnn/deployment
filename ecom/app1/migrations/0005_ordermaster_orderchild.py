# Generated by Django 5.1.4 on 2025-01-20 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordermaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('total', models.FloatField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.reg_form')),
            ],
        ),
        migrations.CreateModel(
            name='orderchild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('total', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.productad')),
                ('oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ordermaster')),
            ],
        ),
    ]
