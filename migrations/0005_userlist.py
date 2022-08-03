# Generated by Django 3.2.9 on 2022-08-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_auto_20220801_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, help_text='The first name of the user.', max_length=200)),
                ('last_name', models.CharField(blank=True, help_text='The last name of the user.', max_length=200)),
                ('email', models.EmailField(help_text='The email and username of the user. Required.', max_length=255, unique=True, verbose_name='email address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
