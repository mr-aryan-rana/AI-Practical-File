import pandas as pd
import numpy as np

print("Name : Aryan Rana \nRoll No : 1323223")
# Example DataFrame
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [np.nan, 11, 12, 13]
}

df = pd.DataFrame(data)
print("Before filling missing values:\n", df)

# Replace missing values with the mean of their columns
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nAfter filling missing values:\n", df)
