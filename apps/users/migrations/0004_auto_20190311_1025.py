# Generated by Django 2.1.7 on 2019-03-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190219_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.png', null=True, upload_to='image/%Y/%m'),
        ),
    ]