import pandas as pd

df = pd.read_csv('clean_sales.csv')

# Total sales and profit
print("=== OVERALL SUMMARY ===")
print(f"Total Sales:  ${df['sales'].sum():,.2f}")
print(f"Total Profit: ${df['profit'].sum():,.2f}")
print(f"Profit Margin: {(df['profit'].sum() / df['sales'].sum() * 100):.1f}%")

# Sales by category
print("\n=== SALES BY CATEGORY ===")
print(df.groupby('category')['sales'].sum().sort_values(ascending=False))

# Sales by region
print("\n=== SALES BY REGION ===")
print(df.groupby('region')['sales'].sum().sort_values(ascending=False))

# Top 5 most profitable products
print("\n=== TOP 5 PROFITABLE PRODUCTS ===")
print(df.groupby('product_name')['profit'].sum().sort_values(ascending=False).head())
