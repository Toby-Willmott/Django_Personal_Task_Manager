# Generated by Django 5.2.1 on 2025-06-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='helo', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
