strategies = ["Always Cooperate", "Always Defect", "Always Change", "Tit for Tat", "Random"]
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
        super(Player, self).__init__()
        self.status = 'defect'
    
    def strategy(self):
        self.status = 'defect'

class CooperativePlayer(Player):
    """
        This player always is cooperative
    """
    def __init__(self):
        super(Player, self).__init__()
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
        super(Player, self).__init__()
        self.status = 'cooperate'
        
        
        # last_gain is a list, that holds gains from previous moves
        self.last_gain = []
    
    def strategy(self):
        if self.points-sum(self.last_gain) == 0:
            self.status = 'defect'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.points-sum(self.last_gain) == 1:
            self.status = 'defect'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.points-sum(self.last_gain) == 3:
            self.status = 'cooperate'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.points-sum(self.last_gain) == 5:
            self.status = 'cooperate'
            self.last_gain.append(self.points-sum(self.last_gain))


class RandomPlayer(Player):
    
    def __init__(self):
        super(Player, self).__init__()
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
        
        if choice == 1:
            self.player1 = DefectivePlayer()
        if choice == 2:
            self.player1 = CooperativePlayer()
        if choice == 3:
            self.player1 = TitForTatPlayer()
        if choice == 4:
            self.player1 = RandomPlayer()

        choice2 = int(input("""
Player 2 chooses:

1. Always defect.
2. Always Cooperate
3. Tit for Tat
4. Random
        
        
        """))
        
        if choice == 1:
            self.player2 = DefectivePlayer()
        if choice == 2:
            self.player2 = CooperativePlayer()
        if choice == 3:
            self.player2 = TitForTatPlayer()
        if choice == 4:
            self.player2 = RandomPlayer()

        print("PLAYER2 IS Random")
        self.player2 = RandomPlayer()
        
        
    def play(self, rounds):
        for r in range(rounds):
            print("\nRound ", r)
            print("\nPLAYER1 chose to " , self.player1.status)
            print("\nPLAYER2 chose to " , self.player2.status)
            if self.player1.status == "cooperate" and self.player2.status == "cooperate":
                player1.gain = 3
                player2.gain = 3
            elif self.player1.status == "cooperate" and self.player2.status == "defect":
                player1.gain = 0
                player2.gain = 5
            elif self.player1.status == "defect" and self.player2.status == "cooperate":
                player1.gain = 5
                player2.gain = 0
            else:
                player1.gain = 1
                player2.gain = 1
            
            player1.points += player1.gain
            player2.points += player2.gain
            player1.strategy()
            player2.strategy()          
            print("\nPLAYER1 gains ", player1.gain, " point, and now has ", player1.points, " points")
            print("\nPLAYER2 gains ", player2.gain, " point, and now has ", player2.points, " points")

    
def main():
    print("Sth, sth, sth, explanation")
    game = Game()
    rounds = int(input("How many rounds: "))
    game.play(rounds)


main()




