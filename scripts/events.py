import csv
from django.db.models import Q
from teams.models import Team, Player
from matches.models import Match
from django.core.exceptions import ObjectDoesNotExist


def run():
    with open('matches.csv') as f:
        events = csv.DictReader(f, delimiter=";")

        current_match = ''
        match = None

        for row in events:
            if row['Fixture'] != current_match:
                current_match = row['Fixture']

            player = Player.objects.select_related('nationality').get(
                nationality__country=row['teamName'].replace('-', ' '),
                number=row['jersey'])

            if row['didScore'] == 'didScore':
                player.goals += 1
            elif row['didAssist'] == 'didAssist':
                player.assists += 1
            elif row['yellowCard'] == 'yellowCard':
                player.yellow_cards += 1
            elif row['redCard'] == 'redCard':
                player.red_cards += 1

            player.save()

