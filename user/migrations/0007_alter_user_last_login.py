# Generated by Django 5.1.1 on 2024-10-17 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 13, 44, 53, 909772), editable=False, verbose_name='last login'),
        ),
    ]