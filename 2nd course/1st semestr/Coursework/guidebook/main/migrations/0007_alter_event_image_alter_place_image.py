# Generated by Django 4.1.4 on 2023-12-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_event_image_alter_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='main/static/main/img/event/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='main/static/main/img/place/'),
        ),
    ]