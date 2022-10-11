# Generated by Django 4.0.4 on 2022-06-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0003_alter_leisureseat_stairs_alter_standardseat_stairs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leisureseat',
            name='floor',
            field=models.CharField(max_length=100, verbose_name='所在楼层'),
        ),
        migrations.AlterField(
            model_name='leisureseat',
            name='power',
            field=models.IntegerField(default=0, verbose_name='拥有电源'),
        ),
        migrations.AlterField(
            model_name='leisureseat',
            name='stairs',
            field=models.IntegerField(default=0, verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='floor',
            field=models.CharField(max_length=100, verbose_name='所在楼层'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='power',
            field=models.IntegerField(default=0, verbose_name='拥有电源'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='stairs',
            field=models.IntegerField(default=0, verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='studyroomseat',
            name='floor',
            field=models.CharField(max_length=100, verbose_name='所在楼层'),
        ),
        migrations.AlterField(
            model_name='studyroomseat',
            name='power',
            field=models.IntegerField(default=0, verbose_name='拥有电源'),
        ),
        migrations.AlterField(
            model_name='studyroomseat',
            name='stairs',
            field=models.IntegerField(default=0, verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='totalseat',
            name='Leisure',
            field=models.CharField(max_length=1000, verbose_name='休闲座位'),
        ),
        migrations.AlterField(
            model_name='totalseat',
            name='Standard',
            field=models.CharField(max_length=1000, verbose_name='标准座位'),
        ),
        migrations.AlterField(
            model_name='totalseat',
            name='StudyRoom',
            field=models.CharField(max_length=1000, verbose_name='自习室座位'),
        ),
    ]
