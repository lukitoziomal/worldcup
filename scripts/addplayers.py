import csv
from teams.models import Team, Player


def format_name(name):
    final_name = ''
    for word in name.split('-'):
        final_name += word[0].upper() + word[1:] + '-'
    return final_name.rstrip('-')


def run():
    with open('players.csv') as players:
        reader = csv.DictReader(players)

        """
        # - shirt number
        POS - position
        PLAYER NAME - name
        FIRST NAME - first name
        LAST NAME - last name
        SHIRT NAME - shirt name
        TEAM - nationality
        """

        current_team = ''
        team = None

        for row in reader:
            country, short = row['TEAM'].split()
            country = country.replace('-', ' ')
            if current_team != country:
                current_team = country
                team, created = Team.objects.get_or_create(
                    country=country,
                    short=short
                )

            if len(row['PLAYER NAME'].split()) > 1:
                name = ''
                for part in row['PLAYER NAME'].split():
                    if part.isupper():
                        name += part.capitalize()
                    else:
                        name = part.capitalize() + name
                player_name = ''.join([' ' + x if x.isupper() else x for x in name]).lstrip()
                if '-' in player_name:
                    player_name = format_name(player_name)
            else:
                player_name = row['PLAYER NAME'].capitalize()

            Player.objects.create(
                name=player_name,
                shirt_name=row['SHIRT NAME'],
                nationality=team,
                number=row['#']
            )