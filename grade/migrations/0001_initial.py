# Generated by Django 3.2.16 on 2022-11-07 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_auto_20221103_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('insufficient', 'insufficient'), ('sufficient', 'sufficient'), ('good', 'good'), ('verygood', 'verygood'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=12)),
                ('type_of_activity', models.CharField(choices=[('Test paper', 'Test paper'), ('Listening', 'Listening')], max_length=12)),
                ('date', models.DateField()),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]