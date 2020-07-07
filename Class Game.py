strategies = ["Always Cooperate", "Always Defect", "Always Change", "Tit for Tat", "Random"]

class Game(object):
    def __init__(self):
        print("Choose first strategy,\n")
        player1_strategy = ask_for_strategy()
        while player1_strategy not in strategies:
            print("There is no such strategy,\n")
            player1_strategy = ask_for_strategy()
            
        print("Choose second strategy,\n")
        player2_strategy = ask_for_strategy():
        while player2_strategy not in strategies:
            print("There is no such strategy,\n")
            player2_strategy = ask_for_strategy()
            
        player1_points = 0
        player2_points = 0
        rounds = int(input("How many rounds: ")

    def ask_for_strategy(self):
        response = None
        response = input("Viable strategies: ", strategies)
        return response


    def play(self):
        for r in rounds:
            status_player1 = status.player1
            status_player2 = status.player2
            if status_player1 == "cooperate" and status_player2 == "cooperate":
                player1_gain = 3
                player2_gain = 3
            elif state_player1 == "cooperate" and status_player2 == "defect":
                player1_gain = 0
                player2_gain = 5
            elif status_player1 == "defect" and status_player2 == "cooperate":
                player1_gain = 5
                player2_gain = 0
            else:
                player1_gain = 1
                player2_gain = 1
            player1_points += player1_gain
            player2_points += player2_gain
            print("\nRound ", r)
            print("\nFirst strategy chose to " , status_player1)
            print("\nSecond strategy chose to " , status_player2)
            print("\nFirst strategy gains ", player1_gain, " point, and now has ", player1_points, " points")
            print("\nSecond strategy now has ", player2_gain, " point, and now has ", player2_points, " points")
            player1.adapt()
            player2.adapt()


def main():
    print("Sth, sth, sth, explanation")
    game = Game()
    game.play()







