# Generated by Django 3.1 on 2020-08-18 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=128, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан в')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания')),
                ('v_type', models.CharField(choices=[('s', 'Одиночный выбор'), ('m', 'Множественный выбор'), ('t', 'Текстовый выбор')], default='s', max_length=1, verbose_name='Тип варианта')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='VoteVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=128, null=True, verbose_name='Текст')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='vote.votequestion')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='VoteAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Строковое значение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='vote.votequestion')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_answers', to=settings.AUTH_USER_MODEL)),
                ('variants', models.ManyToManyField(blank=True, null=True, related_name='answers', to='vote.VoteVariant')),
            ],
            options={
                'verbose_name': 'Ответ пользователя',
                'verbose_name_plural': 'Ответ пользователей',
                'ordering': ['-created_at'],
            },
        ),
    ]