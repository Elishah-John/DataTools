import pandas as pd
import numpy as np

def missing_values(df):
    return df.isnull().sum()

def drop_col(df,col):
    df = df.copy()
    df = df.drop(col, axis=1)
    return df
    
def drop_row(df,row):
    df= df.copy()
    df= df.drop(row, axis=0)
    return df

def to_datetime(df, date_columns):
    df = df.copy()
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df
    
def to_numeric(df, numeric_columns):
    df = df.copy()
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def replace_nan(df):
    df = df.fillna(df.median(numeric_only= True))
    
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].fillna("Unknown")

def clean_dataframe(df, numeric_columns=None, date_columns=None, binary_like_cols = None, cat_fill_value="Unknown", row_na_thresh=0.5):
    df = df.copy()

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    if date_columns:
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    if numeric_columns:
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].fillna(cat_fill_value)

    if binary_like_cols:
        for col in binary_like_cols:
            if col in df.columns:
                df[col] = df[col].map({1: 'Yes', 0: 'No', np.nan: 'Not Recorded', 'Unknown':'Unknown'})

    df = df.dropna(thresh=int(len(df.columns) * (1 - row_na_thresh)))

    return df
