# Generated by Django 5.1.4 on 2025-01-19 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_productad_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('qty', models.IntegerField()),
                ('total', models.FloatField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.productad')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.reg_form')),
            ],
        ),
    ]
