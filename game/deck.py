from card import Card

class Deck:
    def __init__(self):
        self.suits = 'hdsc'
        self.cards = {}
        for suit in self.suits:
            suit_cards = [Card(rank, suit, value) for value, rank in enumerate('A23456789TJQK', start=1)]
            for card in suit_cards:
                self.cards[f"{card.rank}{card.suit}"] = card

    def get_card(self, card_string_rep):
        return self.cards[card_string_rep]

    def __str__(self):
        return ' '.join([str(self.cards[card]) for card in self.cards])