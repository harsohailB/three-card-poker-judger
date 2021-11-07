import fileinput
from game import Game

def main():
    num_players, players_info = 0, []
    
    for index, input in enumerate(fileinput.input()):
        if index == 0:
            num_players = int(input.strip())
        else:
            players_info.append(input.strip())

    game = Game(num_players, players_info)

    winners = game.calculate_winners()

    print(' '.join([winner.id for winner in winners]))

if __name__ == "__main__":
    main()