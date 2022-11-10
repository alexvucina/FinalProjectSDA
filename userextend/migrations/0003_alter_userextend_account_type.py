# Generated by Django 3.2.16 on 2022-11-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0002_userextend_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextend',
            name='account_type',
            field=models.CharField(choices=[('Parent', 'Parent'), ('Teacher', 'Teacher')], default=None, max_length=7),
        ),
    ]