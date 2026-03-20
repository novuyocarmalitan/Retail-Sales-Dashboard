import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clean_sales.csv')
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Superstore Sales Analysis', fontsize=16, fontweight='bold')

# Chart 1: Sales by category
cat = df.groupby('category')['sales'].sum().sort_values()
axes[0,0].barh(cat.index, cat.values, color=['#4C72B0','#DD8452','#55A868'])
axes[0,0].set_title('Sales by Category')
axes[0,0].set_xlabel('Total Sales ($)')

# Chart 2: Sales by region
reg = df.groupby('region')['sales'].sum().sort_values()
axes[0,1].bar(reg.index, reg.values, color='#4C72B0')
axes[0,1].set_title('Sales by Region')
axes[0,1].set_ylabel('Total Sales ($)')

# Chart 3: Monthly sales trend
monthly = df.groupby('month')['sales'].sum()
axes[1,0].plot(monthly.index.astype(str), monthly.values, color='#4C72B0', linewidth=2)
axes[1,0].set_title('Monthly Sales Trend')
axes[1,0].set_xlabel('Month')
axes[1,0].tick_params(axis='x', rotation=45)

# Chart 4: Profit by category
prof = df.groupby('category')['profit'].sum().sort_values()
colors = ['#d9534f' if v < 0 else '#55A868' for v in prof.values]
axes[1,1].barh(prof.index, prof.values, color=colors)
axes[1,1].set_title('Profit by Category')
axes[1,1].set_xlabel('Total Profit ($)')

plt.tight_layout()
plt.savefig('sales_charts.png', dpi=150)
print("Charts saved as sales_charts.png")
