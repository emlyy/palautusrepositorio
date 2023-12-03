class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        self.score = ""

        if self.tied():
            self.tied_score()
        elif self.more_than_four_points():
            self.check_for_winner_and_advantage()
        else:
            self.count_score()

        return self.score

    def tied(self):
        return self.m_score1 == self.m_score2

    def point_difference(self):
        return self.m_score1 - self. m_score2

    def more_than_four_points(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4
    
    def game_over(self):
        return self.point_difference() >= 2 or self.point_difference() <= -2

    def check_for_winner_and_advantage(self):
        if self.game_over():
            self.score = self.winner()
        else:
            self.score = self.advantage()

    def advantage(self):
        if self.point_difference() > 0:
            return "Advantage player1"
        return "Advantage player2"

    def winner(self):
        if self.point_difference() >= 2:
            return "Win for player1"
        return "Win for player2"

    def tied_score(self):
        ties = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        if self.m_score1 < 3:
            score = ties[self.m_score1]
            self.score = score
        else:
            self.score = "Deuce"

    def count_score(self):
        temp_score = 0
        scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                self.score = self.score + "-"
                temp_score = self.m_score2

            self.score = self.score + scores[temp_score]
