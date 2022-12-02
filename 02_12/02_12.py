class Player:
    def __init__(self):
        self.score=0

    def print_score(self):
        print(self.score)

def read_input(input):
    with open(input, "r") as file:
        round_outcomes=[]
        for line in file.readlines():
            round_outcomes.append(line.strip())
    return round_outcomes


def interpret_outcome(letter1, letter2, player1, player2):
    guide = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    if guide[letter1] > guide[letter2]:
        #6 points for player 1
        player1.score += 6 + guide[letter1]
        player2.score += guide[letter2]
    elif guide[letter1] < guide[letter2]:
        # 6 points for player 2
        player2.score += 6 + guide[letter2]
        player1.score += guide[letter1]
    else:
        # draw, 3 points for both player
        player1.score += 3 + guide[letter1]
        player2.score += 3 + guide[letter2]

def count_score(round_outcomes):
    for round in round_outcomes:
        player1_move, player2_move = round.split()
        interpret_outcome(player1_move, player2_move, player1, player2)


player1=Player()
player2=Player()

round_outcomes=read_input("input.txt")
count_score(round_outcomes)

player1.print_score()
player2.print_score()

