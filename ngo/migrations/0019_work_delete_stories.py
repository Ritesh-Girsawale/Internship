# Generated by Django 5.1.7 on 2025-04-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0018_stories_delete_story1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='image/default.jpg', upload_to='image')),
                ('info', models.TextField(default='ww', verbose_name='Details')),
                ('info2', models.TextField(default='ww', verbose_name='Details')),
                ('title', models.CharField(default='ww', max_length=200, verbose_name='Title')),
            ],
        ),
        migrations.DeleteModel(
            name='Stories',
        ),
    ]
