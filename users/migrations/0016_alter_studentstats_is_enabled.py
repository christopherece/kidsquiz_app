# Generated by Django 4.2.11 on 2024-03-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_studentstats_is_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentstats',
            name='is_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
