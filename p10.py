import pandas as pd
print("Name : Krishna \nRoll No : 1323215")
# Load dataset
df = pd.read_csv("myntra.csv")

# If category is in 'product_link' like 'tshirts/brand/product-name' ---
# Extract category from product_link
df['category'] = df['product_link'].apply(lambda x: x.split('/')[0])
filtered_df = df[(df['discounted_price'] > 2000) & (df['category'] == 'tshirts')]

# Show the result
print(filtered_df)
