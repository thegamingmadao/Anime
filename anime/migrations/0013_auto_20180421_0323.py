# Generated by Django 2.0.4 on 2018-04-21 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_episodeurl_movieurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieurl',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.Movie'),
        ),
    ]
