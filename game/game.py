from deck import Deck
from player import Player

class Game:
    """
    This class represents a Three Card Poker Game

    Attributes
    ----------
    deck : Deck
        Deck to be used in the game
    num_players : int
        Number of players playing in the game
    players : list[Player]
        Players playing in the poker game

    Methods
    -------
    create_players(player_inputs): list[Player]
        Creates players for the game using string representation
        of the players
    calculate_winner(): list[Player]
        Calculates the winner(s) of the game
    compare_players(first_player, second_player): Player
        Compares to players based on their hands
    compare_high_cards(first_player, second_player): Player
        Compares the high cards of two players
    __str__(): string
        Creates a string representation of the game object
    """

    def __init__(self, num_players, player_inputs):
        """
        Parameters
        ----------
        num_players : int
            Number of players to attend the game
        players_inputs : list[str]
            String representions of the players 
        """
        if num_players == 0:
            raise Exception("No players given as input to the game!")

        if num_players != len(player_inputs):
            raise Exception("Mismatch between number of players and lines of players given!")

        self.deck = Deck.instance()
        self.num_players = num_players
        self.players = self.create_players(player_inputs)

    def create_players(self, player_inputs):
        """
        Creates players objects using string representations of
        players

        Parameters
        ----------
        player_inputs: list[string]
            String representations of players
        """
        players = []

        for player_input in player_inputs:
            player_info = player_input.split(' ')
            player_cards_info = player_info[1:]
            player_id = player_info[0]

            cards = []
            for card_string in player_cards_info:
                cards.append(self.deck.get_card(card_string))

            players.append(Player(player_id, cards))

        return players

    def calculate_winners(self):
        """
        Calculates the winner(s) from the players in the game
        by comparing their hands
        """
        if(self.num_players == 1):
            return [self.players[0]]

        winners = [self.players[0]]
        
        for i in range(1, len(self.players)):
            curr_player = self.players[i]
            temp_winner = self.compare_players(winners[0], curr_player)
            if temp_winner == None: # tie between curr player and curr winner
                winners.append(curr_player)
            elif temp_winner.id == curr_player.id: # curr player has better hand
                winners = [curr_player]
            
            # if curr winner has better hand, simply proceed to check next player
        
        return winners

    def compare_players(self, first_player, second_player):
        """
        Compares the hand of two players based on its value such as
        straight flush, flush, straight, pair, etc. Return the player
        who won or None to represent a tie.

        Parameters
        ----------
        first_player: Player
            First player to compared
        second_player: Player
            Second player to compared
        """
        if first_player.hand.value > second_player.hand.value:
            return first_player
        elif first_player.hand.value < second_player.hand.value:
            return second_player

        # Check high cards on tie
        return self.compare_high_cards(first_player, second_player)

    def compare_high_cards(self, first_player, second_player):
        """
        Compares hands of two players based on the high cards
        values. Looks at next best card if high cards are the same
        until a higher card is found one player. If not, returns
        None to show a tie.

        Parameters
        ----------
        first_player: Player
            First player to compared
        second_player: Player
            Second player to compared
        """
        first_player_card_vals = first_player.hand_values
        second_player_card_vals = second_player.hand_values

        for i in range(len(first_player_card_vals)):
            first_val, second_val = first_player_card_vals[i], second_player_card_vals[i]
            if first_val > second_val:
                return first_player
            elif first_val < second_val:
                return second_player
            
        return None

    def __str__(self):
        """
        Constructs a string representation of the game object
        """
        output = "----------\n"
        output += f"Number of players: {self.num_players}\n"

        for player in self.players:
            output += f"{str(player)}\n"

        output += "\n----------\n"

        return output