# Generated by Django 3.0.2 on 2020-07-18 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BANKING_MODEL', '0005_auto_20200718_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_type',
            old_name='Employed',
            new_name='account_type',
        ),
        migrations.RemoveField(
            model_name='account_type',
            name='Student',
        ),
        migrations.RemoveField(
            model_name='account_type',
            name='UnEmployed',
        ),
    ]