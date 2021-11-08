from enum import Enum

class Hand(Enum):
    """
    An enum to represent type of hands in Mark43
    three card poker

    <type of hand, value of hand>

    Higher value means strong hand which can beat hands
    of lower value than itself
    """
    HIGH_CARD = 1
    PAIR = 2
    FLUSH = 3
    STRAIGHT = 4
    THREE_OF_A_KIND = 5
    STRAIGHT_FLUSH = 6