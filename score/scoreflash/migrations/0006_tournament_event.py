# Generated by Django 2.2.16 on 2023-08-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0005_auto_20230811_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='event',
            field=models.TextField(null=True),
        ),
    ]