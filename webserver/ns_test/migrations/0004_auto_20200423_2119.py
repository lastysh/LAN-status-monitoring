# Generated by Django 3.0.5 on 2020-04-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ns_test', '0003_auto_20200423_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ips',
            name='comment',
            field=models.CharField(default='', max_length=128, verbose_name='备注'),
        ),
    ]