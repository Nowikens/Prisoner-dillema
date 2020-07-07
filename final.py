strategies = ["Always Cooperate", "Always Defect", "Always Change", "Tit for Tat", "Random"]
import random



# -------------------------------------- PLAYERS -------------------- #


class DefectivePlayer():
    """
        This player always is defective
    """
    def __init__(self):
        self.status = 'defect'
        self.points = 0
    
    def strategy(self):
        self.status = 'defect'

class CooperativePlayer():
    """
        This player always is cooperative
    """
    def __init__(self):
        self.status = 'cooperate'
        self.points = 0
    
    def strategy(self):
        self.status = 'cooperate'

class TitForTatPlayer():
    """
        This player answers to other player's moves.
        If other player cooperates, this player cooperates in next move.
        If other player defects, this player defects in next move.
    """
    def __init__(self):
        self.status = 'cooperate'
        self.points = 0
        
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


class RandomPlayer():
    
    def __init__(self):
        self.possible_status = ('defect', 'cooperate')
        self.status = random.choice(self.possible_status)
        self.points = 0
        
    def strategy(self):
        self.possible_status = ('defect', 'cooperate')
        self.status = random.choice(self.possible_status)




# ------------------------- GAME ------------------------------------- #

class Game():
    def __init__(self):
        print("PLAYER1 IS TitForTat")
        self.player1 = TitForTatPlayer()

        print("PLAYER2 IS TitForTat")
        self.player2 = RandomPlayer()
        

        
    def play(self, rounds):
        for r in range(rounds):
            if self.player1.status == "cooperate" and self.player2.status == "cooperate":
                self.player1_gain = 3
                self.player2_gain = 3
            elif self.player1.status == "cooperate" and self.player2.status == "defect":
                self.player1_gain = 0
                self.player2_gain = 5
            elif self.player1.status == "defect" and self.player2.status == "cooperate":
                self.player1_gain = 5
                self.player2_gain = 0
            else:
                self.player1_gain = 1
                self.player2_gain = 1
            
            self.player1.points += self.player1_gain
            self.player2.points += self.player2_gain
            self.player1.strategy()
            self.player2.strategy()
            print("\nRound ", r)
            print("\nPLAYER1 chose to " , self.player1.status)
            print("\nPLAYER2 chose to " , self.player2.status)
            print("\nPLAYER1 gains ", self.player1_gain, " point, and now has ", self.player1.points, " points")
            print("\nPLAYER2 gains ", self.player2_gain, " point, and now has ", self.player2.points, " points")

    
def main():
    print("Sth, sth, sth, explanation")
    game = Game()
    rounds = int(input("How many rounds: "))
    game.play(rounds)


main()




