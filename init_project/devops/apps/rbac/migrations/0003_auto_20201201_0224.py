# Generated by Django 2.2.2 on 2020-11-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20201201_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roles',
            name='slug',
        ),
        migrations.AlterField(
            model_name='menus',
            name='url',
            field=models.CharField(help_text='精确URL与前端匹配不好包含正则', max_length=128, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='permissions',
            name='url',
            field=models.CharField(max_length=128, verbose_name='含正则的URL'),
        ),
    ]
