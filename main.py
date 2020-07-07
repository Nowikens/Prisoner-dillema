import random




# Prisoner's dillema game


class DefectivePplayer():
    def __init__(self):
        self.status = 'defect'
        self.points = 0
    
    def strategy(self):
        self.status = 'defect'

class CooperativePlayer():
    def __init__(self):
        self.status = 'cooperate'
        self.points = 0
    
    def strategy(self):
        self.status = 'cooperate'

class TitForTatPlayer():
    def __init__(self):
        self.status = 'cooperate'
        self.points = 0
        self.last_gain = []
    
    def strategy(self):
        if self.last_gain == []:
            self.status = 'cooperate'
            self.last_gain = [self.points]
        elif self.last_gain[-1] == 0:
            self.status = 'defective'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.last_gain[-1] == 1:
            self.status = 'defective'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.last_gain[-1] == 3:
            self.status = 'cooperate'
            self.last_gain.append(self.points-sum(self.last_gain))
        elif self.last_gain[-1] == 5:
            self.status = 'cooperate'
            self.last_gain.append(self.points-sum(self.last_gain))


class RandomPlayer():
    possible_status = ('defect', 'cooperate')
    def __init__(self):
        self.status = random.choice(possible_status)
        
    def strategy(self):
        self.status = random.choice(possible_status)
        
        
player1 = TitForTatPlayer()

player1.points = 3
player1.strategy()
print(player1.status)
print(player1.points)
print(player1.last_gain)

player1.points += 1
player1.strategy()
print(player1.status)
print(player1.points)
print(player1.last_gain)

player1.points += 5
player1.strategy()
print(player1.status)
print(player1.points)
print(player1.last_gain)


player1.points += 3
player1.strategy()
print(player1.status)
print(player1.points)
print(player1.last_gain)


player1.points += 0
player1.strategy()
print(player1.status)
print(player1.points)
print(player1.last_gain)