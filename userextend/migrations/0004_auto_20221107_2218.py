# Generated by Django 3.2.16 on 2022-11-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0003_alter_userextend_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextend',
            name='email_confirmation',
        ),
        migrations.AlterField(
            model_name='userextend',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
    ]
