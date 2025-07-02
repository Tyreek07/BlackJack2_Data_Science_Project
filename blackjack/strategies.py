import random

def strategy_manual(game):
    while True:
        print("Player Hand:", game.player.getHand())
        print("Dealer Hand:", game.dealer.getHand())

        playerDecision = input("Hit (h) or Stand (s): ").strip().lower()
        if playerDecision == 'h':
            game.playerHit()
            if game.player.isBusted():
                break
        else:
            break

def strategy_random(game):
    while not game.player.isBusted():
        if random.choice([True, False]):
            game.playerHit()
        else:
            break

def strategy_copy_dealer(game):
    def hasSoft17(game):
        total = 0 
        aces = 0
        for card in game.player.hand:
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

    
    while True:
        score = game.player.getPoints()

        if score < 17 or (score == 17 and hasSoft17(game)):
            game.playerHit()
        else:
            break

def strategy_ai(game):
    pass