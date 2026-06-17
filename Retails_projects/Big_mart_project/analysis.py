# import pandas as pd

# df = pd.read_csv("data/cleaned_bigmart_data.csv")   # apni file ka naam

# def total_sales(df):
#     total = df['OutletSales'].sum()
#     print("Total Sales:", round(total, 2))

# def average_sales(df):
#     avg = df['OutletSales'].mean()
#     print("Average Sales:", round(avg, 2))

# def top_categories(df):

#     top = df.groupby('ProductType')['OutletSales'].sum()
#     top = top.sort_values(ascending=False)
#     print(top.head(10))

# def outlet_sales(df):

#     outlet = df.groupby('OutletType')['OutletSales'].sum()
#     outlet = outlet.sort_values(ascending=False)
#     print(outlet)

# def fat_content_sales(df):

#     fat = df.groupby('FatContent')['OutletSales'].sum()
#     print(fat)    


# total_sales(df)
# average_sales(df)
# top_categories(df)
# outlet_sales(df)
# fat_content_sales(df)

import pandas as pd
import os

# reports folder create karega agar exist nahi karta
os.makedirs("reports", exist_ok=True)

df = pd.read_csv("data\cleaned_bigmart_data.csv")

# functions
def total_sales(df):
    return df['OutletSales'].sum()

def average_sales(df):
    return df['OutletSales'].mean()

def top_categories(df):
    return df.groupby('ProductType')['OutletSales'].sum().sort_values(ascending=False)

def outlet_sales(df):
    return df.groupby('OutletType')['OutletSales'].sum().sort_values(ascending=False)

def fat_content_sales(df):
    return df.groupby('FatContent')['OutletSales'].sum().sort_values(ascending=False)

# Save reports
with open("reports/summary.txt", "w") as f:
    f.write(f"Total Sales: {total_sales(df):.2f}\n")
    f.write(f"Average Sales: {average_sales(df):.2f}\n")

top_categories(df).to_csv("reports/top_categories.csv")
outlet_sales(df).to_csv("reports/outlet_sales.csv")
fat_content_sales(df).to_csv("reports/fat_content_sales.csv")