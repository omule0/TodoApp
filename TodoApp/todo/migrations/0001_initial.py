# Generated by Django 4.2.1 on 2023-06-04 11:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='task', max_length=255)),
                ('due_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('due_time', models.TimeField(blank=True, default=datetime.time(12, 0), null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, default='my todo task', null=True)),
                ('completed', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=False)),
                ('remind_minutes', models.IntegerField(default=5)),
                ('is_skipped', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('week_of', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-week_of'],
            },
        ),
    ]
