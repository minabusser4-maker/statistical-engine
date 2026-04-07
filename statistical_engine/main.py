from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import json

# Load dataset
with open("data/sample_salaries.json") as f:
    data = json.load(f)

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Outliers:", engine.get_outliers())

# Monte Carlo simulation
for days in [30, 365, 10000]:
    prob = simulate_crashes(days)
    print(f"{days} days -> Crash Probability: {prob}")