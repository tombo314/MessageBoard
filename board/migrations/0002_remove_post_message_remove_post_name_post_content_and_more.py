# Generated by Django 5.2.1 on 2025-05-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='未設定', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
