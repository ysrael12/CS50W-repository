# Generated by Django 2.2.14 on 2020-07-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_bid_comment_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('winner', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
                ('winprice', models.IntegerField()),
            ],
        ),
    ]