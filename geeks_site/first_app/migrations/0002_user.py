# Generated by Django 4.1.7 on 2023-03-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
            ],
        ),
    ]