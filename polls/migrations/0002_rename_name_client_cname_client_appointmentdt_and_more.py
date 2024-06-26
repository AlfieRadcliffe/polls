# Generated by Django 4.2.13 on 2024-06-26 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='cname',
        ),
        migrations.AddField(
            model_name='client',
            name='appointmentdt',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 11, 17, 35, 315468)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='cphone',
            field=models.CharField(default=datetime.datetime(2024, 6, 26, 11, 17, 48, 549690), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='issent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stylist',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 26, 11, 17, 57, 488697)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stylist',
            name='message',
            field=models.TextField(default=datetime.datetime(2024, 6, 26, 11, 18, 5, 563365)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stylist',
            name='phone',
            field=models.CharField(default=datetime.datetime(2024, 6, 26, 11, 18, 8, 591451), max_length=20),
            preserve_default=False,
        ),
    ]