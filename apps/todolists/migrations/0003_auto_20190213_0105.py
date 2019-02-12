# Generated by Django 2.1.7 on 2019-02-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0002_todo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['priority', 'add_time'], 'verbose_name': '待完成事项', 'verbose_name_plural': '待完成事项'},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='user',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='todo',
            name='contents',
            field=models.TextField(verbose_name='待做事项'),
        ),
    ]
