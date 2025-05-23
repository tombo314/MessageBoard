# Generated by Django 5.2.1 on 2025-05-16 15:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='投稿者名')),
                ('message', models.TextField(verbose_name='メッセージ')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
            ],
            options={
                'verbose_name': '投稿',
                'verbose_name_plural': '投稿一覧',
                'ordering': ['-created_at'],
            },
        ),
    ]
