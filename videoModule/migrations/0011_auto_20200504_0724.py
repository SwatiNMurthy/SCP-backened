# Generated by Django 3.0.5 on 2020-05-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoModule', '0010_videocontent_speaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocontent',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='videocontent',
            name='resourceType',
        ),
        migrations.AlterField(
            model_name='videocontent',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]