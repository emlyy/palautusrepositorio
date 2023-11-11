class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.games = dict['games']
        self.penalties = dict['penalties']
    
    def __str__(self):
        return (
            f"{self.name} nationality: {self.nationality} "
            f"team: {self.team} games: {self.games} "
            f"assists: {self.assists} goals: {self.goals} "
            f"penalties: {self.penalties}"
            )
