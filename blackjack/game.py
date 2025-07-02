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

    def getCard(self):
        return self.cards.pop()
    
class Player:
    def __init__(self):
        self.hand = []

    def drawCard(self, card):
        self.hand.append(card)

    def getHand(self):
        return self.hand
    
    def resetHand(self):
        self.hand = []

    def getPoints(self):
        points = 0
        aces = 0

        for point in self.hand:
            if point == 11:
                aces+=1
                points += point
            else:
                points += point

        while points > 21 and aces:
            points -= 10
            aces -= 1
        
        return points
    
    def hasBlackJack(self):
        hasBlackJack = False
        for card in self.hand:
            if card == 11:
                hasBlackJack = True
        return hasBlackJack
    
    def isBusted(self):
        points = self.getPoints()
        if points > 21:
            return True
        else:
            return False
 
class Dealer(Player):
    def __init__(self):
        super().__init__()

    def hasSoft17(self):
        total = 0 
        aces = 0
        for card in self.hand:
            if card == 11:
                aces += 1
                total +=11
            else:
                total += card

        while total > 21 and aces:
            total -=10
            aces -=1
        
        if total == 17 and aces:
            return True
        else:
            return False

    
    def playTurn(self, deck):
        while True:
            score = self.getPoints()

            if score < 17 or (score == 17 and self.hasSoft17()):
                self.drawCard(deck.getCard())
            else:
                break

class BlackJackGame:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()
        
        self.deck.shuffleDeck()

    def dealInitialCards(self):
        self.player.drawCard(self.deck.getCard())
        self.player.drawCard(self.deck.getCard())
        self.dealer.drawCard(self.deck.getCard())

    def playerHit(self):
        self.player.drawCard(self.deck.getCard())

    def playerStand(self):
        self.dealer.playTurn(self.deck)

    def getResult(self):
        playerScore = self.player.getPoints()
        dealerScore = self.dealer.getPoints()

        if self.player.isBusted():
            return "loss"
        elif self.dealer.isBusted():
            return "win"

        if playerScore > dealerScore:
            return "win"
        elif playerScore < dealerScore:
            return "loss"
        else:
            return "draw"

    def resetGame(self):
        self.player.resetHand()
        self.dealer.resetHand()
        self.deck = Deck()
        self.deck.shuffleDeck()

    def getState(self):
        return {
            "playerHand": self.player.getHand().copy(),
            "dealerHand": self.dealer.getHand().copy(),
            "playerPoints": self.player.getPoints(),
            "dealerPoints": self.dealer.getPoints()
        }