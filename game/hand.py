from enum import Enum

class Hand(Enum):
    HIGH_CARD = 1
    PAIR = 2
    FLUSH = 3
    STRAIGHT = 4
    THREE_OF_A_KIND = 5
    STRAIGHT_FLUSH = 6