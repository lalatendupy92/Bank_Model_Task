# Generated by Django 3.0.2 on 2020-07-18 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BANKING_MODEL', '0007_auto_20200718_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='user_photo',
        ),
    ]