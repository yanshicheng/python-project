# Generated by Django 2.2.2 on 2020-11-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20201201_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='method_type',
            field=models.IntegerField(choices=[(0, 'GET'), (1, 'POST'), (2, 'PUT'), (3, 'PATCH'), (4, 'DELETE')], default=0, help_text='请求的类型', verbose_name='请求类型'),
        ),
    ]