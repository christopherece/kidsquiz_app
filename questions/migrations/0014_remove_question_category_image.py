# Generated by Django 4.2 on 2023-06-09 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_question_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category_image',
        ),
    ]