from card import Card
from player import Player


class Game:
    def __init__(self, num_players, player_inputs):
        if num_players != len(player_inputs):
            raise Exception("Mismatch between number of players and lines of players given!")

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

    def calculate_winner(self):
        winners = [self.players[0]]

        for i in range(1, len(self.players)):
            curr_player = self.players[i]
            result = self.compare_players(winners[0], curr_player)

            if result == 1: # curr player has better hand
                winners = [curr_player]
            elif result == 0: # tie between curr player and curr winner
                winners.append(curr_player)
            # if curr winner has better hand, simply proceed to check next player

    def compare_players(self, first_player, second_player):
        if first_player.hand_level > second_player.hand_level:
            return -1
        elif first_player.hand_level < second_player.hand_level:
            return 1
        
        return 0 # tie

    def __str__(self):
        output = "----------\n"
        output += f"Number of players: {self.num_players}\n"

        for player in self.players:
            output += f"{str(player)}\n"

        output += "\n----------\n"

        return output