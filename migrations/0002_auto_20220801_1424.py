# Generated by Django 3.2.9 on 2022-08-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='user',
        ),
        migrations.AddField(
            model_name='books',
            name='listed',
            field=models.BooleanField(default=False),
        ),
    ]