# Generated by Django 4.1.2 on 2022-10-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_student_integral'),
    ]

    operations = [
        migrations.CreateModel(
            name='black_user',
            fields=[
                ('User_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='学号')),
                ('timeStatus', models.CharField(default=0, max_length=1000)),
            ],
        ),
    ]