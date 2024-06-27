# Generated by Django 5.0.4 on 2024-06-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('singer', models.CharField(max_length=1000)),
                ('tags', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('song', models.FileField(upload_to='images')),
            ],
        ),
    ]
