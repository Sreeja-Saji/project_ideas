# Generated by Django 4.2.1 on 2023-06-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=220)),
            ],
        ),
        migrations.DeleteModel(
            name='Master',
        ),
    ]
