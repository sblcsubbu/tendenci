# Generated by Django 3.2.18 on 2023-02-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_memberships', '0027_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpprofile',
            name='account_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
