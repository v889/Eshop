# Generated by Django 4.0.2 on 2022-08-24 09:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210508_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
