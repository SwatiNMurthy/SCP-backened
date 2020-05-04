# Generated by Django 3.0.5 on 2020-05-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoModule', '0007_auto_20200502_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocontent',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='videocontent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='videoModule.VideoContent'),
        ),
    ]