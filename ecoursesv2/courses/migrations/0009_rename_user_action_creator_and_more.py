# Generated by Django 4.1.3 on 2022-11-23 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_rename_lesson_comment_lesson_rating_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='user',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user',
            new_name='creator',
        ),
    ]