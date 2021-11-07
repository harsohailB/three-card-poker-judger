from card import Card

# Singleton Deck class as there should only
# be one deck in a game
class Deck:
    suits = 'hdsc'
    deck_instance = None
    cards = None

    def __init__(self):
        raise RuntimeError("Call instance() instead. This is a singleton class.")

    @classmethod
    def instance(cls):
        if cls.deck_instance is None:
            cls.deck_instance = cls.__new__(cls)
            cls.deck_instance.create_cards()
            
        return cls.deck_instance
    
    def create_cards(self):
        cards_dict = {}

        for suit in self.suits:
            suit_cards = [Card(rank, suit, value) for value, rank in enumerate('A23456789TJQK', start=1)]
            for card in suit_cards:
                cards_dict[f"{card.rank}{card.suit}"] = card

        self.cards = cards_dict

    def get_card(self, card_string_rep):
        return self.cards[card_string_rep]

    def __str__(self):
        return ' '.join([str(self.cards[card]) for card in self.cards])
