from deck import Deck
from hand import Hand
from player import Player


class Game:
    def __init__(self, num_players, player_inputs):
        if num_players == 0:
            raise Exception("No players given as input to the game!")

        if num_players != len(player_inputs):
            raise Exception("Mismatch between number of players and lines of players given!")

        self.num_players = num_players
        self.players = self.create_players(player_inputs)

    def create_players(self, player_inputs):
        players = []

        for player_input in player_inputs:
            player_info = player_input.split(' ')
            player_cards_info = player_info[1:]
            player_id = player_info[0]

            cards = []
            for card_string in player_cards_info:
                cards.append(Deck.get_card(card_string))

            players.append(Player(player_id, cards))

        return players

    def calculate_winners(self):
        if(self.num_players == 1):
            return [self.players[0].id]

        winners = [self.players[0]]

        for i in range(1, len(self.players)):
            curr_player = self.players[i]
            temp_winner = self.compare_players(winners[0], curr_player)

            if temp_winner.id == curr_player.id: # curr player has better hand
                winners = [curr_player]
            elif temp_winner == None: # tie between curr player and curr winner
                winners.append(curr_player)
            # if curr winner has better hand, simply proceed to check next player
        
        return [player.id for player in winners]

    def compare_players(self, first_player, second_player):
        if first_player.hand.value > second_player.hand.value:
            return first_player
        elif first_player.hand.value < second_player.hand.value:
            return second_player
        
        # Check high cards on tie
        high_card_winner = self.compare_high_cards(first_player, second_player)

        return high_card_winner if high_card_winner else None

    def compare_high_cards(self, first_player, second_player):
        is_pairs = first_player.hand == Hand.PAIR
        first_player_card_vals = first_player.get_card_values_for_high_card()
        second_player_card_vals = second_player.get_card_values_for_high_card()

        if is_pairs: # use pair high rules
            first_player_card_vals = list(set(first_player_card_vals))
            second_player_card_vals = list(set(second_player_card_vals))

        for i in range(len(first_player_card_vals)):
            first_val, second_val = first_player_card_vals[i], second_player_card_vals[i]
            if first_val > second_val:
                return first_player
            elif first_val < second_val:
                return second_player
            
        return None


    def __str__(self):
        output = "----------\n"
        output += f"Number of players: {self.num_players}\n"

        for player in self.players:
            output += f"{str(player)}\n"

        output += "\n----------\n"

        return output