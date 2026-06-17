import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/cleaned_bigmart_data.csv")

##top categories
top = df.groupby('ProductType')['OutletSales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top.plot(kind='bar')
plt.title("Top 10 Product Categories by Sales")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("charts/top_categories.png")
plt.close()

## fatcontent sales


fat = df.groupby('FatContent')['OutletSales'].sum()

plt.figure(figsize=(6,4))
fat.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Sales by Fat Content")

plt.savefig("charts/fat_content_sales.png")
plt.close()

##outlets 
outlet = df.groupby('OutletType')['OutletSales'].sum()

plt.figure(figsize=(8,5))
outlet.plot(kind='bar')
plt.title("Sales by Outlet Type")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("charts/outlet_sales.png")
plt.close()

## mrp distibution 


plt.figure(figsize=(8,5))
plt.hist(df['MRP'], bins=30)

plt.title("MRP Distribution")
plt.xlabel("MRP")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("charts/mrp_distribution.png")
plt.close()