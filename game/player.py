from collections import Counter
from hand import Hand

class Player:
    def __init__(self, id, cards):
        if len(cards) != 3:
            raise Exception(f"Player {id} does not have 3 cards!")
        
        self.id = id
        self.cards = cards
        self.evaluate_hand()

    def evaluate_hand(self):
        self.hand_values = self.get_card_values_for_high_card()

        # Check for pair or three of a kind
        card_ranks_freq = Counter([card.rank for card in self.cards])
        num_cards_same_ranks = card_ranks_freq[max(card_ranks_freq, key=card_ranks_freq.get)]
        if num_cards_same_ranks == 2: 
            self.hand = Hand.PAIR
            return
        elif num_cards_same_ranks == 3: 
            self.hand = Hand.THREE_OF_A_KIND
            return

        is_flush = self.check_flush()
        is_straight, self.hand_values = self.check_straight()
        
        if is_flush and is_straight:
            self.hand = Hand.STRAIGHT_FLUSH
        elif is_flush:
            self.hand = Hand.FLUSH
        elif is_straight:
            self.hand = Hand.STRAIGHT
        else:
            self.hand = Hand.HIGH_CARD

    def check_straight(self):
        possibilites = self.get_card_values_for_straight()
        for card_values in possibilites:
            is_straight = True
            for i in range(len(card_values) - 1):
                curr_rank, next_rank = card_values[i], card_values[i + 1]
                if abs(next_rank - curr_rank) != 1:
                    is_straight = False
            if is_straight:
                return True, card_values
                    
        return False, self.hand_values

    def check_flush(self):
        card_suits_freq = Counter([card.suit for card in self.cards])
        num_cards_same_suit = card_suits_freq[max(card_suits_freq, key=card_suits_freq.get)]
        if num_cards_same_suit == 3: 
            return True
        return False

    def get_card_values_for_straight(self):
        # Possiblies for A usage on both sides
        possibilites = [sorted([card.value for card in self.cards], reverse=True)]
        if 1 in possibilites[0]:
            possibilites.append(sorted([card.value if card.value != 1 else 14 for card in self.cards], reverse=True))
        return possibilites

    def get_card_values_for_high_card(self):
        return [sorted([card.value if card.value != 1 else 14 for card in self.cards], reverse=True)]

    def __str__(self):
        return f"{self.id} - {' '.join([str(card) for card in self.cards])} - {self.hand} - {self.hand_values}"
