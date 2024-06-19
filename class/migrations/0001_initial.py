# Generated by Django 5.0.6 on 2024-06-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_lecture', models.CharField(max_length=20)),
                ('class_capacity', models.PositiveSmallIntegerField()),
                ('class_name', models.CharField(max_length=20)),
                ('class_time', models.TimeField()),
                ('class_id', models.PositiveSmallIntegerField()),
            ],
        ),
    ]