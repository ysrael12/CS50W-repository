# Generated by Django 3.2.9 on 2021-11-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20211129_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
