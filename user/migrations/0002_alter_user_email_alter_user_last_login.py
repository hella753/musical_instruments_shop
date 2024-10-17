# Generated by Django 5.1.1 on 2024-10-17 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 13, 34, 2, 569863), editable=False, verbose_name='last login'),
        ),
    ]
