import pandas as pd

# df = pd.read_csv("data/Train.csv")


# # Show first 5 rows
# print(df.head())

# # Dataset information
# print(df.info())

# #   for checking null or empty value
# import pandas as pd

# df = pd.read_csv("data/Train.csv")

# print(df.isnull().sum())


## again check null value

# import pandas as pd
# from cleaning import clean_data

# # Load dataset
# df = pd.read_csv("data/Train.csv")

# # Clean dataset
# df = clean_data(df)

# # Check missing values again
# print(df.isnull().sum())

# ## check fat content 
# print(df['FatContent'].unique())

# # dataset check info
# print(df.info())

### after cleaning data
# import pandas as pd
# from cleaning import clean_data

# # Load dataset
# df = pd.read_csv("data/Train.csv")

# # Clean dataset
# df = clean_data(df)

# # Check dataset
# print(df.head())

# print(df.isnull().sum())

# print(df['FatContent'].unique())

# # # Save cleaned data
# df.to_csv("data/cleaned_bigmart_data.csv", index=False)

# print("Data cleaning completed.")

# print(df.columns)



### data of insights 

import pandas as pd

from cleaning import clean_data

from analysis import (
    total_sales,
    average_sales,
    top_categories,
    outlet_sales,
    fat_content_sales
)

# Load dataset
df = pd.read_csv("data/cleaned_bigmart_data.csv")

# Clean columns
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Clean data
df = clean_data(df)

## save to reports 
# top.to_csv("reports/top_categories.csv")
# print("Data save to reports completed.")

# Analysis
total_sales(df)

average_sales(df)

top_categories(df)

outlet_sales(df)

fat_content_sales(df)


top_categories = (
    df.groupby("ProductType")["OutletSales"]
    .sum()
    .sort_values(ascending=False)
)

outlet_sales = (
    df.groupby("OutletType")["OutletSales"]
    .sum()
    .sort_values(ascending=False)
)

fat_content_sales = (
    df.groupby("FatContent")["OutletSales"]
    .sum()
    .sort_values(ascending=False)
)

with pd.ExcelWriter("reports/bigmart_report.xlsx") as writer:
    top_categories.to_excel(writer, sheet_name="Top Categories")
    outlet_sales.to_excel(writer, sheet_name="Outlet Sales")
    fat_content_sales.to_excel(writer, sheet_name="Fat Content")

print("Excel report created successfully!")
