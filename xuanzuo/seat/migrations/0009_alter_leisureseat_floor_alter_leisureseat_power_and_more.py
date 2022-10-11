# Generated by Django 4.0.4 on 2022-06-11 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0008_alter_studyroomseat_floor_alter_studyroomseat_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leisureseat',
            name='floor',
            field=models.CharField(help_text='座位所在楼层', max_length=50, verbose_name='所在楼层'),
        ),
        migrations.AlterField(
            model_name='leisureseat',
            name='power',
            field=models.IntegerField(default=0, help_text='座位电源状态，1表示靠近电源，0表示不靠近电源', verbose_name='拥有电源'),
        ),
        migrations.AlterField(
            model_name='leisureseat',
            name='stairs',
            field=models.IntegerField(default=0, help_text='座位靠近楼梯，1表示靠近，0表示不靠近', verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='leisureseat',
            name='status',
            field=models.IntegerField(default=0, help_text='座位状态，0是空，1表示已预约', verbose_name='座位状态'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='floor',
            field=models.CharField(help_text='座位所在楼层', max_length=50, verbose_name='所在楼层'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='power',
            field=models.IntegerField(default=0, help_text='座位电源状态，1表示靠近电源，0表示不靠近电源', verbose_name='拥有电源'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='stairs',
            field=models.IntegerField(default=0, help_text='座位靠近楼梯，1表示靠近，0表示不靠近', verbose_name='靠近走廊'),
        ),
        migrations.AlterField(
            model_name='standardseat',
            name='status',
            field=models.IntegerField(default=0, help_text='座位状态，0是空，1表示已预约', verbose_name='座位状态'),
        ),
    ]
