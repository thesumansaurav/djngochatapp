# Generated by Django 4.0.1 on 2022-01-11 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='ContextManager',
            new_name='content',
        ),
    ]
