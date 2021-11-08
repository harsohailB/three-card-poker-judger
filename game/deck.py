from card import Card

class Deck:
    """
    A singleton class that represents the deck to be
    used in the game

    Attributes
    ----------
    suits : string
        Characters representing the suits of a deck
    deck_instance : Deck
        Single instance of the singleton Deck class
    cards : list[Card]
        Cards in the deck

    Methods
    -------
    instance(cls): Deck
        Singleton constructor of the Deck class
    create_cards()
        Creates cards of the deck
    get_card(card_string_rep):
        Returns card object based on string reprentation of the card
    __str__(): string
        Creates a string representation of the deck object
    """
    suits = 'hdsc'
    deck_instance = None
    cards = None

    def __init__(self):
        """
        Placeholder contructor for the class that throws an error when called
        as custom instance() constructor is to be used for a singleton class
        """
        raise RuntimeError("Call instance() instead. This is a singleton class.")

    @classmethod
    def instance(cls):
        """
        A class method to be the singleton constructor which creates a deck object if not
        existing before, and otherwise returns the previously created object to maintain
        singleton behaviour
        """
        if cls.deck_instance is None:
            cls.deck_instance = cls.__new__(cls)
            cls.deck_instance.create_cards()
            
        return cls.deck_instance
    
    def create_cards(self):
        """
        Creates card objects for the deck using suits and card ranks
        """
        cards_dict = {}

        for suit in self.suits:
            suit_cards = [Card(rank, suit, value) for value, rank in enumerate('A23456789TJQK', start=1)]
            for card in suit_cards:
                cards_dict[f"{card.rank}{card.suit}"] = card

        self.cards = cards_dict

    def get_card(self, card_string_rep):
        """
        Gets a card object from the deck

        Parameters
        ----------
        card_string_rep : string
            String representation of a card (as given in stdin)
        """
        return self.cards[card_string_rep]

    def __str__(self):
        """
        Constructs a string representation of the deck object
        """
        return ' '.join([str(self.cards[card]) for card in self.cards])
