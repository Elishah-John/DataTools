import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visual_relation(df, plot_type, title, size, x, y,**kwargs):
    plt.figure(figsize=size)
    plot_type(df,  x=x, y=y, **kwargs)
    plt.title(title)

def correlation_matrix(df,fields,size,title):
    correlation = df[fields].corr()

    mask = np.triu(np.ones_like(correlation, dtype=bool))

    plt.figure(figsize=size)
    sns.heatmap(correlation, 
                mask=mask,
                annot=True, 
                cmap='coolwarm',
                fmt='.2f',
                vmin=-1, vmax=1,
                center=0)

    plt.title(title, pad=10)
    plt.tight_layout()
    plt.show()

def data_distribution(df, title, kde=False, remove_col = None):
    df = df.copy()
    if remove_col:
        df = df.drop(remove_col, axis=1)
    plt.title(title)
    sns.histplot(df, kde = kde)
    plt.show()
    
    