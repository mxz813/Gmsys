# Generated by Django 2.1.7 on 2019-02-25 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0006_auto_20190218_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['is_done', 'priority', 'add_time'], 'verbose_name': '待完成事项', 'verbose_name_plural': '待完成事项'},
        ),
    ]
