# Generated by Django 4.2.7 on 2023-12-03 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_task_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='list.tag'),
            preserve_default=False,
        ),
    ]
