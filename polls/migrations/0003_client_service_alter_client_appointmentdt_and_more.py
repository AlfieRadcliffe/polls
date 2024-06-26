# Generated by Django 4.2.13 on 2024-06-26 10:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_name_client_cname_client_appointmentdt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='service',
            field=models.CharField(default=datetime.datetime(2024, 6, 26, 11, 28, 52, 703522), max_length=20, verbose_name='Service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='appointmentdt',
            field=models.DateTimeField(verbose_name='Time and Date of appointment'),
        ),
        migrations.AlterField(
            model_name='client',
            name='cname',
            field=models.CharField(max_length=100, verbose_name='Client Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='cphone',
            field=models.CharField(max_length=11, verbose_name='Client Phone Number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='issent',
            field=models.BooleanField(default=False, verbose_name='Has a message been Sent?'),
        ),
        migrations.AlterField(
            model_name='client',
            name='stylist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.stylist', verbose_name='Stylist Name'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date / Time'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Stylist Name'),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Stylist Phone Number'),
        ),
    ]
