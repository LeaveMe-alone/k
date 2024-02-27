# Generated by Django 5.0.1 on 2024-02-24 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_postx_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('intro', models.TextField()),
                ('paragraph_1', models.TextField()),
                ('my_back_quote', models.TextField()),
                ('subheading', models.TextField()),
                ('paragraph_2', models.TextField()),
                ('paragraph_3', models.TextField()),
                ('conclusion', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.DeleteModel(
            name='Postx',
        ),
    ]