import numpy as np
import pandas as pd

players = ["Virat", "Rohit", "Dhoni", "Rahul", "Hardik"]
runs = np.array([8000, 6500, 10000, 4500, 3000])

print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))

df = pd.DataFrame({
    "Player": players,
    "Runs": runs
})

print("\nPlayer Statistics:")
print(df)

print("\nPlayers with more than 5000 runs:")
print(df[df["Runs"] > 5000])
