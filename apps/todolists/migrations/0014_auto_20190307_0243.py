# Generated by Django 2.1.7 on 2019-03-07 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0013_usualtodo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usualtodo',
            options={'ordering': ['priority', 'add_time'], 'verbose_name': '日常计划', 'verbose_name_plural': '日常计划'},
        ),
    ]
