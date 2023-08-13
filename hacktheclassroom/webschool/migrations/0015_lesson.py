# Generated by Django 4.2.3 on 2023-08-09 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webschool', '0014_delete_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_thumbnail', models.ImageField(upload_to='lesson_thumb/')),
                ('lesson_name', models.CharField(max_length=200)),
                ('lesson_url', models.URLField(blank=True, max_length=300)),
                ('lesson_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webschool.teacher')),
                ('grade_for', models.ManyToManyField(to='webschool.grade')),
                ('lesson_tags', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webschool.tag')),
            ],
        ),
    ]