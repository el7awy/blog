# Generated by Django 2.0.2 on 2018-04-12 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='article',
        ),
    ]
