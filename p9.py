import pandas as pd
print("Name : Aryan Rana \nRoll No : 1323223")
# Load the Myntra dataset
df = pd.read_csv("myntra.csv")  # change filename if needed

# Display the first few rows
print(df.head(1), "\n")

# --- 1️: Dataset info ---
print("=== Dataset Info ===")
print(df.info(), "\n")

# --- 2️: Shape ---
print("=== Shape (Rows, Columns) ===")
print(df.shape, "\n")

# --- 3️: Describe ---
print("=== Statistical Summary ===")
print(df.describe(), "\n")

# --- 4️: Check for Null Values ---
print("=== Null Values ===")
print(df.isnull().sum(), "\n")

# --- 5️: Calculate Total Revenue and Total Discount ---
df["Revenue"] = df["discounted_price"]
df["Discount"] = df["marked_price"] - df["discounted_price"]

total_revenue = df["Revenue"].sum()
total_discount = df["Discount"].sum()

print("=== Totals ===")
print(f"💰 Total Revenue: ₹{total_revenue:,.2f}")
print(f"🤑 Total Discount Given: ₹{total_discount:,.2f}")
