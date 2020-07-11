import random



# -------------------------------------- PLAYERS -------------------- #

class Player():
    def __init__(self):
        self.points = 0
        self.gain = 0
    
class DefectivePlayer(Player):
    """
        This player always is defective
    """
    def __init__(self):
        super(DefectivePlayer, self).__init__()
        self.status = 'defect'
    
    def strategy(self):
        self.status = 'defect'

class CooperativePlayer(Player):
    """
        This player always is cooperative
    """
    def __init__(self):
        super(CooperativePlayer, self).__init__()
        self.status = 'cooperate'
        
    
    def strategy(self):
        self.status = 'cooperate'

class TitForTatPlayer(Player):
    """
        This player answers to other player's moves.
        If other player cooperates, this player cooperates in next move.
        If other player defects, this player defects in next move.
    """
    def __init__(self):
        super(TitForTatPlayer, self).__init__()
        self.status = 'cooperate'
        
        
        # last_gain is a list, that holds gains from previous moves
        self.last_gain = []
    
    def strategy(self):
        if self.points-sum(self.last_gain) == 0 or self.points-sum(self.last_gain) == 1:
            self.status = 'defect'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.points-sum(self.last_gain) == 3 or self.points-sum(self.last_gain) ==5:
            self.status = 'cooperate'
            self.last_gain.append(self.points-sum(self.last_gain))
       


class RandomPlayer(Player):
    
    def __init__(self):
        super(RandomPlayer, self).__init__()
        self.possible_status = ('defect', 'cooperate')
        self.status = random.choice(self.possible_status)
        self.points = 0
        
    def strategy(self):
        self.possible_status = ('defect', 'cooperate')
        self.status = random.choice(self.possible_status)




# ------------------------- GAME ------------------------------------- #
class Game():
    def __init__(self):
        print(
"""
Hello there, You're in jail. We have your partner. This jail makes no sens so instead of years in prison, you gain points.
That's right, points. If you two bastards cooperate, you both get 3 points. If you defect and your partner cooperates you
get 5 points, and he gets 0, if he defects while you cooperate, you get 0 and he gets 5. 

NOW CHOOSE ONE OF BELOW STRATEGIES.        
"""
)
        
        choice1 = int(input("""
Player 1 chooses:

1. Always defect.
2. Always Cooperate
3. Tit for Tat
4. Random
        
        
        """))
        
        if choice1 == 1:
            self.player1 = DefectivePlayer()
        if choice1 == 2:
            self.player1 = CooperativePlayer()
        if choice1 == 3:
            self.player1 = TitForTatPlayer()
        if choice1 == 4:
            self.player1 = RandomPlayer()

        choice2 = int(input("""
Player 2 chooses:

1. Always defect.
2. Always Cooperate
3. Tit for Tat
4. Random
        
        
        """))
        
        if choice2 == 1:
            self.player2 = DefectivePlayer()
        if choice2 == 2:
            self.player2 = CooperativePlayer()
        if choice2 == 3:
            self.player2 = TitForTatPlayer()
        if choice2 == 4:
            self.player2 = RandomPlayer()

        self.rounds = int(input("How many rounds?"))

        
    def play(self):
        for r in range(self.rounds):
            print("\nRound ", r+1)
            print("\nPLAYER1 chose to " , self.player1.status)
            print("\nPLAYER2 chose to " , self.player2.status)
            if self.player1.status == "cooperate" and self.player2.status == "cooperate":
                self.player1.gain = 3
                self.player2.gain = 3
            elif self.player1.status == "cooperate" and self.player2.status == "defect":
                self.player1.gain = 0
                self.player2.gain = 5
            elif self.player1.status == "defect" and self.player2.status == "cooperate":
                self.player1.gain = 5
                self.player2.gain = 0
            else:
                self.player1.gain = 1
                self.player2.gain = 1
            
            self.player1.points += self.player1.gain
            self.player2.points += self.player2.gain
            self.player1.strategy()
            self.player2.strategy()          
            print("\nPLAYER1 gains ", self.player1.gain, " point, and now has ", self.player1.points, " points")
            print("\nPLAYER2 gains ", self.player2.gain, " point, and now has ", self.player2.points, " points")

    
def main():
    
    game = Game()
    game.play()


main()


input("press Enter to end")

#Other Player classes to add: Checks For Tat, Always Changes, Grudger,...
