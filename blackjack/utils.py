import csv

def saveGame(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def loadCSV(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)


def printHand(hand):
    return ' '.join(str(card) for card in hand)

def calculate_win_rate(results):
    wins = sum(1 for r in results if r['result'] == 'win')
    return wins / len(results) if results else 0.0
