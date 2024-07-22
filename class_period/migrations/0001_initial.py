# Generated by Django 5.0.6 on 2024-07-22 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_week', models.CharField(max_length=20)),
                ('classroom', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_periods', to='course.course')),
            ],
        ),
    ]
