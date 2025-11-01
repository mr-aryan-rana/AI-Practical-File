# Find the average price of products grouped by category.
import pandas as pd
import matplotlib.pyplot as plt
print("Name : Aryan Rana \nRoll No : 1323223")
# Load dataset
df = pd.read_csv("myntra.csv")

# Count number of products per brand
brand_counts = df['brand_name'].value_counts().head(10)

# Plot bar chart
plt.figure(figsize=(6, 6))
brand_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Products per Brand', fontsize=8)
plt.xlabel('Brand', fontsize=8)
plt.ylabel('Number of Products', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
