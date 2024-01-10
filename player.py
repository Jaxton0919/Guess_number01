class Player:
    def __init__(self,s_name):
        self.name = s_name
        self.numPlayed = 0
        self.numWon = 0
        self.numLost = 0
        self.numTied = 0
        self.current_points = 100
    def get_player(self):
        if self.numPlayed == 0:
            return self.name + " has 100 points, and never played a game."
        else:
            return self.name+" has " + self.current_points + " points and a winning rate of " + (self.numWon / self.numPlaye)*100 + "%."