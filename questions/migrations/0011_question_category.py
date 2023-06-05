# Generated by Django 4.2 on 2023-06-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_question_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('addition', 'Addition'), ('subtraction', 'Subtraction'), ('multiplication', 'Multiplication'), ('division', 'Division')], max_length=50),
        ),
    ]