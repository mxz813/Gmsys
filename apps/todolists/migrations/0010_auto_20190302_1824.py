# Generated by Django 2.1.7 on 2019-03-02 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0009_todo_plan_done_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='done_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='完成时间'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='plan_done_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='计划完成时间'),
        ),
    ]
