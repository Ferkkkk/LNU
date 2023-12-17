# Generated by Django 4.1.4 on 2023-12-17 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_event_city_alter_event_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime_end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата та час закінчення'),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата та час початку'),
        ),
    ]