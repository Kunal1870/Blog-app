# Generated by Django 4.1.7 on 2023-02-16 11:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='img')),
                ('body', models.TextField()),
                ('post_id', models.UUIDField(default=uuid.UUID('363a179a-2cbe-416f-8b8d-c642ab9dc192'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]