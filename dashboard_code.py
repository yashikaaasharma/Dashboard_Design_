import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Superstore-style data
data = {
    'Order Date': pd.to_datetime(['2016-11-08', '2016-11-08', '2016-06-12']),
    'Region': ['South', 'South', 'West'],
    'Category': ['Furniture', 'Furniture', 'Office Supplies'],
    'Sub-Category': ['Bookcases', 'Chairs', 'Labels'],
    'Sales': [261.96, 731.94, 14.62],
    'Profit': [41.91, 219.58, 6.87],
    'Quantity': [2, 3, 2]
}

df = pd.DataFrame(data)
sns.set(style="whitegrid")

# Create subplot layout
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Superstore Dashboard - Yashika Sharma", fontsize=16)

# 1. Line Chart: Sales over Time
df_line = df.groupby('Order Date')[['Sales']].sum().reset_index()
sns.lineplot(data=df_line, x='Order Date', y='Sales', ax=axs[0, 0])
axs[0, 0].set_title("Sales Over Time")

# 2. Bar Chart: Sales by Category
df_bar = df.groupby('Category')[['Sales']].sum().reset_index()
sns.barplot(data=df_bar, x='Category', y='Sales', ax=axs[0, 1])
axs[0, 1].set_title("Sales by Category")
axs[0, 1].tick_params(axis='x', rotation=15)

# 3. Pie Chart: Profit by Region
df_pie = df.groupby('Region')[['Profit']].sum()
axs[1, 0].pie(df_pie['Profit'], labels=df_pie.index, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title("Profit Distribution by Region")

# 4. Bar Chart: Quantity by Sub-Category
df_sub = df.groupby('Sub-Category')[['Quantity']].sum().reset_index()
sns.barplot(data=df_sub, x='Sub-Category', y='Quantity', ax=axs[1, 1])
axs[1, 1].set_title("Quantity by Sub-Category")
axs[1, 1].tick_params(axis='x', rotation=15)

# Save and display
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("dashboard_mock_yashika_sharma.png")
plt.show()
