# Generated by Django 3.0.2 on 2020-02-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITBAEvent', '0003_auto_20200208_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='accredit',
            field=models.ManyToManyField(related_name='accredited', to='ITBAEvent.participant'),
        ),
    ]