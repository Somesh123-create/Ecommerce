# Generated by Django 3.2.4 on 2021-06-16 17:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210616_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2021, 6, 16, 17, 18, 59, 714019, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
