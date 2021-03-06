# Generated by Django 3.2.9 on 2021-12-05 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_auto_20211205_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='ratedUsers',
            field=models.ManyToManyField(blank=True, related_name='ratedUsersComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='videos.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='unavailable', max_length=250),
        ),
    ]
