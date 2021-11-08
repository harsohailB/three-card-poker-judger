import fileinput
from game import Game

def main():
    """
    Mark 43 Three Card Poker

    This main function is the entry point to the
    three card poker judger.

    It is responsible for taking and parsing the input
    stream, generating a game object, and outputting
    the winner ids.
    """
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