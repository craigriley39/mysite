# Generated by Django 2.0 on 2017-12-23 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20171223_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 23, 21, 39, 10, 154195)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_fulfill_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 23, 21, 39, 10, 154217)),
        ),
    ]