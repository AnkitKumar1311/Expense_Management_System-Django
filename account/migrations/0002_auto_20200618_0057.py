# Generated by Django 3.0.7 on 2020-06-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/%Y/%m'),
        ),
    ]