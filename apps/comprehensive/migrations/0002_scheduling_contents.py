# Generated by Django 2.1.7 on 2019-03-13 19:16

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comprehensive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduling',
            name='contents',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='排班内容'),
        ),
    ]
