# Generated by Django 2.0.5 on 2018-05-20 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollanswer',
            name='choices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='web.PollChoice', verbose_name='Вариант'),
        ),
    ]
