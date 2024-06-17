# Generated by Django 5.0.6 on 2024-05-29 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='cover_image',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='blog_cover_image', to='blog.coverimage'),
            preserve_default=False,
        ),
    ]
