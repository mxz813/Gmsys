# Generated by Django 2.1.7 on 2019-03-08 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comprehensive', '0002_scheduling_scheduling_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='scheduling_year',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='plans.PlanYear', verbose_name='排班年份'),
        ),
    ]
