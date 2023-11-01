from player import Player

def sort_by_points(player:Player):
    return player.points

def sort_by_goals(player:Player):
    return player.goals

def sort_by_assists(player:Player):
    return player.assists

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, num=1):
        sort_by = SortBy(num).name
        if sort_by == 'POINTS':
            sort_key = sort_by_points
        if sort_by == 'GOALS':
            sort_key = sort_by_goals
        if sort_by == 'ASSISTS':
            sort_key = sort_by_assists
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
