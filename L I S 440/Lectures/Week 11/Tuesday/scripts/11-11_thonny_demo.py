# Import the necessary packages
import pandas as pd # because 6 characters is to much
import os
from pathlib import Path # to set up paths easier

# Print version of pandas
print(pd.__version__)

# Set working directory (CWD) : root folder
root = Path(__file__).parent.parent.resolve()

# Show current working directory
print("Current Working Directory: ",Path.cwd())

# Set CWD: Data
data = root / 'data'
# Set CWD: Data > Raw
data_raw = data / 'raw'
# Set CWD: Data > Processed
data_processed = root / 'data' / 'processed'
# Set CWD: Scripts
scripts = root / 'scripts'


# Read Student Data
wisc_data = data_processed / 'StateHousing2023_wisconsin.csv'

# Create dataframe of student data
wisc_df = pd.read_csv(wisc_data) # He labeled it wisconsinHousingDF but too long


# View first and last 3 entries
print("First 5 rows: \n", wisc_df.head(3)) # just show head
print("Last 5 rows: \n", wisc_df.tail(3)) # check if I am there

# Ask for shape of Function
print("Shape of data: \n", wisc_df.shape)
print("Columns:", wisc_df.columns )

# Get the number of rows and columns using .shape
num_rows, num_cols = wisc_df.shape
print(f"Total number of rows: {num_rows}")
print(f"Total number of columns: {num_cols}")

# Trying out summary stat funcs from https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
print(wisc_df.describe())


# Following what prof does:
print("Last 2 rows: \n", wisc_df.tail(2))

valueColumnSeries = wisc_df["Value"] 
print("Value Column: ", valueColumnSeries)

# Convert the Value column from String to Numeric
# 1. Remove the '$' and ',' characters
wisc_df['Value'] = wisc_df['Value'].str.replace(r'[$,]', '', regex=True)
# 2. Convert the cleaned column to a numeric type
wisc_df['Value'] = pd.to_numeric(wisc_df['Value']) # numeric to then be able to calculate mean, etc
print(wisc_df.head(1)) # check if convert successfull

# Print the corrected col value entries
print("The Values column has ", valueColumnSeries.size, "entries.")

# Basic summary stats
print("Average Value (Mean):", wisc_df['Value'].mean())
print("Median Value:", wisc_df['Value'].median())
print("Mode Value(s):\n", wisc_df['Value'].mode())

# EDITS PER FEEDBACK
# Missing: (1) print your name, (2) print the whold df
print("Alejandro De La Torre's code...") # fixes prob 1
print(wisc_df) # fixes prob 2


print("End of program.")


