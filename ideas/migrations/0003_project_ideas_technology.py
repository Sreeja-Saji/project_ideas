# Generated by Django 4.2.1 on 2023-06-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_course_delete_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Ideas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Ideas', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Technology', models.CharField(max_length=220)),
            ],
        ),
    ]
