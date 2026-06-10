import pandas as pd

def clean_data(file_path):

    df = pd.read_excel(file_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Unknown")

    # Save cleaned file
    df.to_excel("Reports/cleaned_sales_data.xlsx", index=False)

    return df