# Generated by Django 2.1.7 on 2019-04-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0004_parktwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parktwo',
            name='inside',
            field=models.IntegerField(default=None),
        ),
    ]
