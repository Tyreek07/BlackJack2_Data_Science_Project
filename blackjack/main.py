from simulator import run_simulator
from strategies import (
    strategy_random,
    strategy_copy_dealer,
    strategy_manual 
)

from utils import loadCSV, calculate_win_rate, printHand
import os

os.makedirs("data", exist_ok=True)

strategies = {
    #"random": strategy_random,
    #"dealer": strategy_copy_dealer,
    #"player": strategy_manual  
}

results_summary = {}

for name, strategy in strategies.items():
    print(f"Running {name} strategy...")
    filename = f"data/{name}_strategy.csv"
    run_simulator(strategy=strategy, numGames=100, outputFile=filename)

    data = loadCSV(filename)
    win_rate = calculate_win_rate(data)
    results_summary[name] = win_rate
    print(f"{name} win rate: {win_rate:.2%}")


