# Generated by Django 2.0.4 on 2018-04-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_auto_20180416_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Air_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Monday', max_length=10)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='day',
            field=models.CharField(default='Monday', max_length=10),
        ),
    ]
