# Generated by Django 4.0.4 on 2023-06-27 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_groupteam_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupteam',
            name='teams',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupTeam',
        ),
    ]
