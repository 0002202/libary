# Generated by Django 4.0.4 on 2022-06-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0002_alter_studyroomseat_stairs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leisureseat',
            name='stairs',
            field=models.IntegerField(default=1, verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='stairs',
            field=models.IntegerField(default=1, verbose_name='靠近走廊'),
        ),
    ]
