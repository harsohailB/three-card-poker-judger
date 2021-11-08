class Card:
    """
    A class to represent a card in the game

    Attributes
    ----------
    rank : string
        Rank of the card (A,2,3,...,J,Q,K)
    suit : char
        Suit of the card (s - spades, d - diamonds, c - clubs, etc.)
    value: int
        Value of the card (10 - 10, J - 11, Q - 12, etc.)
    """

    def __init__(self, rank, suit, value):
        """
        Constructor to create the card object

        Parameters
        ----------
        rank : string
        suit : char
        value: int
        """
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        """
        String representation of the card object (same as stdin card representation)
        """
        return f"{self.rank}{self.suit}"