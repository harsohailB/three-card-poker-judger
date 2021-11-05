class Player:
    def __init__(self, id, cards):
        if len(cards) != 3:
            raise Exception(f"Player {id} does not have 3 cards!")
        
        self.id = id
        self.cards = cards


    def __str__(self):
        return f"{self.id} {' '.join([str(card) for card in self.cards])}"
