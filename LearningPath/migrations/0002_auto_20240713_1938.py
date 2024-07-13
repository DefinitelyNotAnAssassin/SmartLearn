# Generated by Django 3.2.6 on 2024-07-13 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LearningPath', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningpath',
            name='path_status',
        ),
        migrations.RemoveField(
            model_name='learningpathtopic',
            name='topic_status',
        ),
        migrations.AlterField(
            model_name='learningpath',
            name='path_code',
            field=models.CharField(default='517bfce', editable=False, max_length=256),
        ),
        migrations.CreateModel(
            name='StudentLearningPathTopicStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress'), ('not_started', 'Not Started')], max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningPath.learningpathtopic')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLearningPathStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress'), ('not_started', 'Not Started')], max_length=100)),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningPath.learningpath')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
