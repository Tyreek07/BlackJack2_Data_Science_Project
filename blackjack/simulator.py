from game import BlackJackGame
from utils import saveGame

def run_simulator(strategy, numGames=10000, outputFile=None):
    results= []
    for _ in range(numGames):
        game = BlackJackGame()
        game.dealInitialCards()

        strategy(game)

        game.playerStand()

        result = game.getResult()
        
        game_data = {
            "playerStartHand": game.player.getHand()[:2],
            "playerdraws": game.player.getHand()[2:],  
            "dealerStartHand": game.dealer.getHand()[:1],
            "dealerDraws": game.dealer.getHand()[1:],
            "result": result,
            "player_points": game.player.getPoints(),
            "dealer_points": game.dealer.getPoints() 
        }

        results.append(game_data)

    if outputFile:
        saveGame(outputFile, results, fieldnames=list(results[0].keys()))

    return results

    