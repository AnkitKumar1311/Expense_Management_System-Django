# Generated by Django 3.0.7 on 2020-06-22 22:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20200621_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 22, 59, 8, 138969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 22, 59, 8, 138969, tzinfo=utc)),
        ),
    ]
