# Generated by Django 4.0.4 on 2022-06-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0004_alter_leisureseat_floor_alter_leisureseat_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leisureseat',
            name='power',
            field=models.CharField(max_length=100, verbose_name='靠近电源'),
        ),
        migrations.AlterField(
            model_name='leisureseat',
            name='stairs',
            field=models.CharField(max_length=100, verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='power',
            field=models.CharField(max_length=100, verbose_name='靠近电源'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='stairs',
            field=models.CharField(max_length=100, verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='studyroomseat',
            name='power',
            field=models.CharField(max_length=100, verbose_name='靠近电源'),
        ),
        migrations.AlterField(
            model_name='studyroomseat',
            name='stairs',
            field=models.CharField(max_length=100, verbose_name='靠近走廊'),
        ),
    ]
