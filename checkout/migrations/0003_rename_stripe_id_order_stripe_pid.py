# Generated by Django 3.2 on 2022-04-19 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20220419_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stripe_id',
            new_name='stripe_pid',
        ),
    ]