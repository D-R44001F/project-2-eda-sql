# Import necessary libraries
import pandas as pd

data = pd.read_csv("./supermarket_dataset/sales.csv")

# Data Exploration
data.head()

# Columns, Value Counts and Types
data.info()

# Sampling a random fraction (20%) of rows from the DataFrame
data.sample(frac=0.2)

# Check for missing values in the DataFrame
missing_values = pd.isnull(data)

# Count missing values in each column
missing_counts = missing_values.sum()

# Count columns with missing values
columns_with_missing = missing_counts[missing_counts > 0].count()

# Check if all columns have missing values
all_columns_missing = missing_counts.all()

# Calculate the total number of missing values
total_missing_values = missing_counts.sum()

# Display the results
print("Missing Values in Each Column:\n", missing_counts)
print("\nNumber of Columns with Missing Values:", columns_with_missing)
print("All Columns Have Missing Values:", all_columns_missing)
print("\nTotal Missing Values in the DataFrame:", total_missing_values)