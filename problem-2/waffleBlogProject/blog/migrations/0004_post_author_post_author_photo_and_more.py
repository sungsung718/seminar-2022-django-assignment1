# Generated by Django 4.1 on 2022-09-29 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='author_photo',
            field=models.ImageField(default='default.jpg', upload_to='upload_photo/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 11, 38, 50, 255590, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
