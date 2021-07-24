# Generated by Django 3.2.5 on 2021-07-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_city',
            field=models.SmallIntegerField(choices=[(0, '北京'), (1, '上海'), (2, '深圳')], verbose_name='工作地点'),
        ),
    ]