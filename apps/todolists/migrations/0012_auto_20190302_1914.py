# Generated by Django 2.1.7 on 2019-03-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0011_auto_20190302_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
    ]
