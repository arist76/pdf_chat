# Generated by Django 5.0.2 on 2024-02-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatmessage_options_alter_pdf_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='type',
            field=models.CharField(choices=[('ai', 'ai'), ('user', 'user')], default='user', max_length=15),
        ),
    ]
