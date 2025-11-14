import pandas as pd
print("Name : Krishna \nRoll No : 1323215")
# Load dataset
df = pd.read_csv("myntra.csv")


# --- If category is in 'product_link' like 'tshirts/brand/product-name' ---
# Extract category
df['category'] = df['product_link'].apply(lambda x: x.split('/')[0])
avg_price = df.groupby('category')['discounted_price'].mean()

# Display the result
print("Average price of products per category:\n")
print(avg_price)
