# Generated by Django 5.1.7 on 2025-04-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_story_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='info',
            field=models.CharField(max_length=300, verbose_name='info'),
        ),
        migrations.AlterField(
            model_name='story',
            name='info2',
            field=models.CharField(default='ww', max_length=300, verbose_name='info2'),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(default='ww', max_length=300, verbose_name='title'),
        ),
    ]
