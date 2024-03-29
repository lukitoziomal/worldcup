# Generated by Django 4.0.4 on 2023-06-27 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_player_shirt_name_team_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('wins', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('teams', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
                ('teams', models.ManyToManyField(to='teams.groupteam')),
            ],
        ),
    ]
