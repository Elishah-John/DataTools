
def summarize_df(df):
   return {
      'Shape': df.shape,
      'Missing Values': df.isnull().sum(),
      'Data Types': df.dtypes
    }

def null_columns(df, threshold=0.3):
    return df.columns[df.isnull().mean() > threshold]

def overview(df):
    return {
        'columns': list(df.columns),
        'missing_values': df.isnull().sum(),
        'dtypes': df.dtypes,
        'head': df.head()
    }
