# Generated by Django 4.0.4 on 2022-11-24 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('wins', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('goals', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('yellow_cards', models.IntegerField(default=0)),
                ('red_cards', models.IntegerField(default=0)),
                ('minutes_played', models.IntegerField(default=0)),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
