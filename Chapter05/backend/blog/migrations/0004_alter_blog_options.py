# Generated by Django 5.0.6 on 2024-06-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_alter_blog_author_alter_blog_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('update_title', 'Can update the title of the blog'), ('update_content', 'Can update the content of blog')]},
        ),
    ]
