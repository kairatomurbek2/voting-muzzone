# Generated by Django 2.0.5 on 2018-05-18 10:14

from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Зоголовок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создание')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='PollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='Ip адресс')),
                ('user_agent', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Зоголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to=main.utils.poll_choices_image_path, verbose_name='Изображение')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='web.Poll')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.AddField(
            model_name='pollanswer',
            name='choices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.PollChoice', verbose_name='Вариант'),
        ),
    ]
