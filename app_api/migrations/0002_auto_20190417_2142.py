# Generated by Django 2.1.7 on 2019-04-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openorder',
            name='order',
            field=models.IntegerField(default=0, verbose_name='开闸指令'),
        ),
    ]
