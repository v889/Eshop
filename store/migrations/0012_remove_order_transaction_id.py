# Generated by Django 4.1 on 2022-08-25 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
    ]
