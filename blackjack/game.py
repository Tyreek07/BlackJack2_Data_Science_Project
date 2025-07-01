import random

class Deck:
    def __init__(self):
        self.cards = []
        
        for i in range(1,5):
            for card in range(2,12):
                self.cards.append(card)
            for card in range(1,5):
                self.cards.append(10)
    
    def shuffleDeck(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()