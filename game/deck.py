from card import Card

class Deck:
    suits = 'hdsc'

    def create_cards(suits):
        cards_dict = {}

        for suit in suits:
            suit_cards = [Card(rank, suit, value) for value, rank in enumerate('A23456789TJQK', start=1)]
            for card in suit_cards:
                cards_dict[f"{card.rank}{card.suit}"] = card

        return cards_dict

    cards = create_cards(suits)

    @staticmethod
    def get_card(card_string_rep):
        return Deck.cards[card_string_rep]

    @staticmethod
    def __str__():
        return ' '.join([str(Deck.cards[card]) for card in Deck.cards])