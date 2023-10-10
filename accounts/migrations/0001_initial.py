# Generated by Django 4.2.6 on 2023-10-10 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일_아이디')),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('birthday', models.DateField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('withdraw_date', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일_아이디')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('birthday', models.DateField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
