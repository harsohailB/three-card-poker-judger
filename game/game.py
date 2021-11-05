from card import Card
from player import Player


class Game:
    def __init__(self, deck, num_players, player_inputs):
        if num_players != len(player_inputs):
            raise Exception("Mismatch between number of players and lines of players given!")

        self.deck = deck
        self.num_players = num_players
        self.players = self.create_players(player_inputs)

    def create_players(self, player_inputs):
        players = []

        for player_input in player_inputs:
            player_info = player_input.split(' ')
            player_cards_info = player_info[1:]
            player_id = int(player_info[0])

            cards = []
            for card_string in player_cards_info:
                cards.append(self.deck.get_card(card_string))

            players.append(Player(player_id, cards))

        return players

    def __str__(self):
        output = "----------\n"
        output += f"Number of players: {self.num_players}\n"

        for player in self.players:
            output += f"{str(player)}\n"

        output += "\n----------\n"

        return output