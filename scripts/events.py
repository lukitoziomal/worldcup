import csv
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from teams.models import Team, Player
from matches.models import Match, Event


def run():
    with open('matches.csv') as f:
        events = csv.DictReader(f, delimiter=";")

        current_match = ''
        match = None

        for row in events:
            if row['Fixture'] != current_match:
                current_match = row['Fixture']
                home, away = Team.objects.filter(
                    Q(country=row['Home Team'].replace('-', ' ')) | Q(country=row['Away Team'].replace('-', ' '))
                )
                match = Match.objects.create(
                    date=row['Date'],
                    stage=row['stage'],
                    home_team=home,
                    away_team=away,
                    home_goals=row['Home Goal'],
                    away_goals=row['Away Goal']
                )
                match.save()

            player = Player.objects.select_related('nationality').get(
                nationality__country=row['teamName'].replace('-', ' '),
                number=row['jersey'])

            event_type = ''

            if row['didScore'] == 'didScore':
                player.goals += 1
                event_type = 'G'
            elif row['didAssist'] == 'didAssist':
                player.assists += 1
                event_type = 'A'
            elif row['yellowCard'] == 'yellowCard':
                player.yellow_cards += 1
                event_type = 'Y'
            elif row['redCard'] == 'redCard':
                player.red_cards += 1
                event_type = 'R'

            player.save()

            if event_type != '':
                event = Event.objects.create(
                    type=event_type,
                    player1=player,
                    clock=row['Clock']
                )
                event.save()
                match.events.add(event)


