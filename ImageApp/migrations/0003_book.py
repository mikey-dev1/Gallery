# Generated by Django 4.1 on 2022-09-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageApp', '0002_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='books/')),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100, unique=True)),
                ('is_published', models.BooleanField(default=True)),
                ('ratings', models.IntegerField()),
            ],
        ),
    ]
