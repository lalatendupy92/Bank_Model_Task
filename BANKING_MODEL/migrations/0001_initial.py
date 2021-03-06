# Generated by Django 3.0.2 on 2020-07-17 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employed', models.CharField(max_length=100)),
                ('UnEmployed', models.CharField(max_length=100)),
                ('Student', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone', models.IntegerField(max_length=10)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_photo', models.ImageField(upload_to='')),
                ('user_account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BANKING_MODEL.Account_type')),
            ],
        ),
    ]
