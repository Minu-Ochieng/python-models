# Generated by Django 5.0.6 on 2024-07-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_name', models.CharField(max_length=100)),
                ('class_code', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('room_allocation', models.CharField(default=0, max_length=100)),
                ('no_of_tables', models.PositiveSmallIntegerField(default=0)),
                ('no_of_students', models.PositiveSmallIntegerField(default=0)),
                ('class_representative', models.CharField(blank=True, max_length=10)),
                ('class_goals', models.TextField(blank=True)),
                ('class_meeting', models.CharField(blank=True, max_length=100)),
                ('period_entity', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
