# 🧰 DataTools
 
**A lightweight Python toolkit for fast, intuitive data cleaning, exploration, and visualization.**

`DataTools` simplifies the messy first steps of data analysis, helping you go from raw data to meaningful insights without rewriting boilerplate code every time.

---

## **📁 Module Overview**

### Data Exploration:
    
- `summarize_df`: Returns a quick overview: shape, number of missing values, and data types.

- `null_columns`: Lists columns where the amount of missing values exceeds the given threshold.

- `overview`: Provides column names, missing value counts, data types, and the first 5 rows — all in one go.

### Data Visualization: 

- `visual_relation`: Plots the relationship between two columns using scatter, line, or other plot types.

- `correlation_matrix`:  Plots a heatmap showing correlations between all numeric fields in the DataFrame.

- `data_distribution`: Plots a histogram (with optional KDE) to visualize the distribution of values in a numeric column.

### Data Cleaning:
 
- `missing_values`: Lists the amount of missing values in each field.

- `drop_col`: Drops the specified columns.
- `drop_row`: Drops the specified rows by index.
- `to_datetime`: Converts a column to datetime format.
- `to_numeric`: Converts a column (even if it's stored as `object`) to proper numeric format.
- `clean_dataframe`: Automatically cleans a DataFrame by:

    - Converting date columns to datetime format

    - Converting numeric strings to actual numbers
    - Replacing binary (like 1/0) with 'Yes'/'No'
    - Filling missing values in categorical fields with 'Unknown'

---

## 📦 Installation

### ▶ Install directly from GitHub:

```bash
pip install git+https://github.com/Elishah-John/DataTools.git
```
### 🛠️ For local development:

```bash
git clone https://github.com/Elishah-John/DataTools.git
cd mydatatools
pip install -e .
```
This installs the package in editable mode so you can modify it and see changes instantly.

## 🧪 Quick Start

```python
import pandas as pd
from DataTools import summarize_df, data_distribution

df = pd.read_csv("your_dataset.csv")

# Give a quick summary of the dataframe
summarize_df(df)

# Plot distribution of a numeric column
data_distribution(df, 'column_name')
```

## **📋 Requirements**

```
pandas
seaborn
matplotlib
numpy
```
### Install them with:

```bash
pip install -r requirements.txt
```


## 📜 License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

If you have any questions or suggestions, feel free to reach out:
- **Email**: elishahjohn9@gmail.com
- **LinkedIn**: http://www.linkedin.com/in/elishah-johnej
