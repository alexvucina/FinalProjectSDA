# Generated by Django 3.2.16 on 2022-11-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0004_auto_20221107_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='userextend',
            name='account_type',
        ),
    ]
