# Generated by Django 2.0.5 on 2018-08-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20180804_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='opportunity_vote',
            field=models.BooleanField(default=True, verbose_name='Возможность голосовать'),
        ),
    ]
