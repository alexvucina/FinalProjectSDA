# Generated by Django 3.2.16 on 2022-11-13 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0008_parent_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='cnp',
        ),
    ]
