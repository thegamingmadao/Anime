# Generated by Django 2.0.4 on 2018-04-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='episode_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
