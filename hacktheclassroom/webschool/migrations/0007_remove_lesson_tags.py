# Generated by Django 4.2.3 on 2023-08-09 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0006_remove_teacher_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='tags',
        ),
    ]