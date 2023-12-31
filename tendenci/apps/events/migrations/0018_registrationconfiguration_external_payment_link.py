# Generated by Django 3.2.12 on 2022-05-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20210917_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationconfiguration',
            name='external_payment_link',
            field=models.URLField(blank=True, default='', help_text='A third party payment link. If specified, online payment will be redirected to it.', verbose_name='External payment link'),
        ),
    ]
