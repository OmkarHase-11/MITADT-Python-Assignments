import numpy as np

# Create a one-dimensional array containing numbers from 1 to 10
arr = np.arange(1, 11)

print("Original Array:", arr)

# Slicing operations
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting - add 5 to every element
arr = arr + 5

print("Array after broadcasting (+5):", arr)
