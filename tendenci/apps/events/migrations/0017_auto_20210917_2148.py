# Generated by Django 2.2.24 on 2021-09-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_place_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='national',
            field=models.BooleanField(default=False, help_text='Is it a national event?'),
        ),
        migrations.AddField(
            model_name='place',
            name='virtual',
            field=models.BooleanField(default=False, help_text='Is it a virtual event?'),
        ),
    ]
