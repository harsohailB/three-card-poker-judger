import fileinput

from deck import Deck
from game import Game

def main():
    num_players, players_info = 0, []
    
    for index, input in enumerate(fileinput.input()):
        if index == 0:
            num_players = int(input.strip())
        else:
            players_info.append(input.strip())

    game = Game(num_players, players_info)
    
    print(game)
    print(game.calculate_winner())

if __name__ == "__main__":
    main()