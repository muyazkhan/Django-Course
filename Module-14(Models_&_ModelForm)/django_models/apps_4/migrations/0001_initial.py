# Generated by Django 5.0 on 2023-12-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('adress', models.TextField()),
            ],
        ),
    ]
