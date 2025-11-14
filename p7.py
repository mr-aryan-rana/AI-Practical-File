import numpy as np
print("Name : Krishna \nRoll No : 1323215")
# Example NumPy array
arr = np.array([2, 5, 8, 10, 12, 15])

# Set threshold
threshold = 10

# Replace elements greater than threshold with the threshold
arr = np.where(arr > threshold, threshold, arr)

print(arr)
