# Generated by Django 5.1.3 on 2024-12-13 12:14

import django.db.models.deletion
import reviews.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_commonreviewdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('commonreviewdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reviews.commonreviewdata')),
                ('runtime', models.DurationField()),
                ('director', models.CharField(max_length=100)),
                ('category', models.ForeignKey(default=reviews.models.Category.film_category, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.category')),
            ],
            bases=('reviews.commonreviewdata',),
        ),
    ]
