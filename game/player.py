from collections import Counter
from hand import Hand

class Player:
    def __init__(self, id, cards):
        if len(cards) != 3:
            raise Exception(f"Player {id} does not have 3 cards!")
        
        self.id = id
        self.cards = cards
        self.evaluate_hand(cards)

    def evaluate_hand(self, cards):
        # Check for pair or three of a kind
        card_ranks_freq = Counter([card.rank for card in cards])
        num_cards_same_ranks = card_ranks_freq[max(card_ranks_freq, key=card_ranks_freq.get)]
        if num_cards_same_ranks == 2: 
            self.hand = Hand.PAIR
            return
        elif num_cards_same_ranks == 3: 
            self.hand = Hand.THREE_OF_A_KIND
            return

        # Check for flush
        is_flush = False
        card_suits_freq = Counter([card.suit for card in cards])
        num_cards_same_suit = card_suits_freq[max(card_suits_freq, key=card_suits_freq.get)]
        if num_cards_same_suit == 3: 
            is_flush = True
        
        # Check for straight
        is_straight = True
        card_values = sorted([card.value for card in cards], reverse=True)
        for i in range(len(card_values) - 1):
            curr_rank, next_rank = card_values[i], card_values[i + 1]
            if curr_rank == 13 and next_rank == 1: continue
            if abs(next_rank - curr_rank) != 1:
                is_straight = False

        if is_flush and is_straight:
            self.hand = Hand.STRAIGHT_FLUSH
        elif is_flush:
            self.hand = Hand.FLUSH
        elif is_straight:
            self.hand = Hand.STRAIGHT
        else:
            self.hand = Hand.HIGH_CARD

    def __str__(self):
        return f"{self.id} - {' '.join([str(card) for card in self.cards])} - {self.hand}"
