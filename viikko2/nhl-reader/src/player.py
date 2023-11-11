class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.games = dict['games']
        self.penalties = dict['penalties']
        self.points = self.goals+self.assists
    
    def __str__(self):
        return (
            f"{self.name} "
            f"team: {self.team} "
            f"assists: {self.assists} goals: {self.goals} "
            f"points: {self.points}"
            )
