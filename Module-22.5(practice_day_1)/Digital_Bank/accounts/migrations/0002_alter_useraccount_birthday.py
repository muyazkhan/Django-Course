# Generated by Django 5.0 on 2023-12-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
