# Generated by Django 4.1.4 on 2023-12-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='City', max_length=255, verbose_name='Місто, населений пункт'),
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(default='Country', max_length=255, verbose_name='Країна'),
        ),
        migrations.AddField(
            model_name='event',
            name='region',
            field=models.CharField(default='Region', max_length=255, verbose_name='Регіон, область'),
        ),
    ]