# Generated by Django 5.1.3 on 2024-12-13 12:21

import django.db.models.deletion
import reviews.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_commonreviewdata_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('commonreviewdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reviews.commonreviewdata')),
                ('studio', models.CharField(max_length=100)),
                ('time_to_beat', models.DurationField()),
                ('number_of_players', models.IntegerField()),
                ('category', models.ForeignKey(default=reviews.models.Category.game_category, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.category')),
            ],
            bases=('reviews.commonreviewdata',),
        ),
        migrations.CreateModel(
            name='TVReview',
            fields=[
                ('commonreviewdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reviews.commonreviewdata')),
                ('number_of_episodes', models.IntegerField()),
                ('showrunner', models.CharField(max_length=100)),
                ('average_episode_length', models.DurationField()),
                ('category', models.ForeignKey(default=reviews.models.Category.tv_category, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.category')),
            ],
            bases=('reviews.commonreviewdata',),
        ),
    ]
