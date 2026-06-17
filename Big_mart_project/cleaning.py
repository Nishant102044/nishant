import pandas as pd

def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing Item_Weight with mean
    df['Weight'] = df['Weight'].fillna(df['Weight'].mean())

    # Fill missing Outlet_Size with mode
    df['OutletSize'] = df['OutletSize'].fillna(df['OutletSize'].mode()[0])

    ## standarize fat content lablels
    df['FatContent'] = df['FatContent'].replace({
        'LF' : 'Low Fat',
        'low fat' : 'Low Fat',
        'reg' : 'Regular'
    })

    return df