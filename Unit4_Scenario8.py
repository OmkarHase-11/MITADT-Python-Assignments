import numpy as np
import pandas as pd

items = ["Rice", "Sugar", "Milk", "Bread", "Oil"]
prices = np.array([60, 40, 30, 25, 150])
quantity = [15, 5, 8, 20, 4]

print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

df = pd.DataFrame({
    "Item": items,
    "Price": prices,
    "Quantity": quantity
})

print("\nGrocery Inventory:")
print(df)

print("\nItems with quantity less than 10:")
print(df[df["Quantity"] < 10])
