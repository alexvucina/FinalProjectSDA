# Generated by Django 3.2.16 on 2022-11-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('0', 'Inactive'), ('1', 'Active')], default=[('0', 'Inactive'), ('1', 'Active')], max_length=8, null=True),
        ),
    ]
