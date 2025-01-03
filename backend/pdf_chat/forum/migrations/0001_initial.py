# Generated by Django 5.0.2 on 2024-03-11 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_slug', models.SlugField(max_length=255)),
                ('description', models.TextField()),
                ('subject', models.CharField(choices=[('biology', 'biology'), ('chemistry', 'chemistry'), ('physics', 'physics'), ('math', 'math'), ('english', 'english'), ('agriculture', 'agriculture')], max_length=150)),
                ('grade', models.CharField(choices=[('9', 'grade nine'), ('10', 'grade ten'), ('11', 'grade eleven'), ('12', 'grade twelve')], max_length=2)),
                ('views', models.IntegerField()),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.room')),
            ],
        ),
    ]
