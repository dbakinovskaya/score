# Generated by Django 3.1.10 on 2023-09-15 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreflash', '0009_auto_20230912_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventid',
            name='live_event_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoreflash.events'),
        ),
    ]
