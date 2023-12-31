# Generated by Django 4.1.4 on 2023-12-17 18:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('kind', models.CharField(max_length=255, verbose_name='Вид')),
                ('type', models.CharField(max_length=255, verbose_name='Тип')),
                ('average_review_score', models.FloatField(default=0, verbose_name='Середня оцінка відгуків')),
                ('description', models.TextField(verbose_name='Опис')),
                ('country', models.CharField(default='Україна', max_length=255, verbose_name='Країна')),
                ('region', models.CharField(default='Львівська область', max_length=255, verbose_name='Регіон, область')),
                ('city', models.CharField(default='Львів', max_length=255, verbose_name='Місто, населений пункт')),
                ('latitude', models.FloatField(default=0, verbose_name='Широта')),
                ('longitude', models.FloatField(default=0, verbose_name='Довгота')),
                ('total_reviews', models.IntegerField(default=0, verbose_name='Кількість відгуків')),
                ('total_score', models.IntegerField(default=0, verbose_name='Загальна оцінка')),
                ('image', models.ImageField(default='default.jpg', upload_to='images/place/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Відгук')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('type', models.CharField(default='Не вказано', max_length=255, verbose_name='Тип')),
                ('description', models.TextField(verbose_name='Опис')),
                ('datetime_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата та час початку')),
                ('datetime_end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата та час закінчення')),
                ('country', models.CharField(default='Україна', max_length=255, verbose_name='Країна')),
                ('region', models.CharField(default='Львівська область', max_length=255, verbose_name='Регіон, область')),
                ('city', models.CharField(default='Львів', max_length=255, verbose_name='Місто, населений пункт')),
                ('latitude', models.FloatField(default=0, verbose_name='Широта')),
                ('longitude', models.FloatField(default=0, verbose_name='Довгота')),
                ('guests', models.TextField(default=' ', verbose_name='Гості')),
                ('image', models.ImageField(default='default.jpg', upload_to='images/event/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.place')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата та час')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
