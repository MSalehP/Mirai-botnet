# Generated by Django 4.2.16 on 2024-10-17 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_remove_systemdata_system_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemdata',
            name='system_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 22, 28, 12, 433842, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
