<<<<<<< HEAD
import pandas as pd

def generate_report(df):

    summary = df.groupby("Product_Category")["Sales_Amount"].sum().reset_index()

    summary.to_excel("Reports/sales_report.xlsx", index=False)

=======
import pandas as pd

def generate_report(df):

    summary = df.groupby("Product_Category")["Sales_Amount"].sum().reset_index()

    summary.to_excel("Reports/sales_report.xlsx", index=False)

>>>>>>> 6442826c615e90312781ce7636378122ee1c4d54
    return summary