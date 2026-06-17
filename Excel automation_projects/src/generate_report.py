import pandas as pd

def generate_report(df):

    summary = df.groupby("Product_Category")["Sales_Amount"].sum().reset_index()

    summary.to_excel("Reports/sales_report.xlsx", index=False)

    return summary