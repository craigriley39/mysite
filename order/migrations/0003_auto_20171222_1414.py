# Generated by Django 2.0 on 2017-12-22 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20171222_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 14, 14, 53, 520796)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_fulfill_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 22, 14, 14, 53, 520821)),
        ),
    ]
