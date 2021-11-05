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

        is_flush = self.check_flush(cards)
        is_straight = self.check_straight(cards)
        
        if is_flush and is_straight:
            self.hand = Hand.STRAIGHT_FLUSH
        elif is_flush:
            self.hand = Hand.FLUSH
        elif is_straight:
            self.hand = Hand.STRAIGHT
        else:
            self.hand = Hand.HIGH_CARD

    def check_straight(self, cards):
        possibilites = self.get_card_values_for_straight(cards)
        is_straights = []
        for card_values in possibilites:
            for i in range(len(card_values) - 1):
                curr_rank, next_rank = card_values[i], card_values[i + 1]
                if abs(next_rank - curr_rank) != 1:
                    is_straights.append(False)
                    
        return len(is_straights) < len(possibilites)

    def check_flush(self, cards):
        card_suits_freq = Counter([card.suit for card in cards])
        num_cards_same_suit = card_suits_freq[max(card_suits_freq, key=card_suits_freq.get)]
        if num_cards_same_suit == 3: 
            return True
        return False

    def get_card_values_for_straight(self, cards):
        # Possiblies for A usage on both sides
        possibilites = [sorted([card.value for card in cards], reverse=True)]
        if 1 in possibilites[0]:
            possibilites.append(sorted([card.value if card.value != 1 else 14 for card in cards], reverse=True))
        return possibilites


    def get_card_values_for_high_card(self):
        return sorted([card.value if card.value != 1 else 14 for card in self.cards], reverse=True)

    def __str__(self):
        return f"{self.id} - {' '.join([str(card) for card in self.cards])} - {self.hand}"
