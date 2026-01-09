# ----------------------------------------
# File & Path Setup
# ----------------------------------------

# Import the necessary packages
import pandas as pd
import os
from pathlib import Path

# Set current working directory (CWD) : root folder
root = Path(__file__).parent.parent.resolve()

# Show CWD
print("Current Working Directory: ", Path.cwd())

# Set CWD: Data
data = root / 'data'
# Set CWD: Data > Raw
data_raw = data / 'raw'
# Set CWD: Data > Processed
data_processed = root / 'data' / 'processed'
# Set CWD: Scripts
scripts = root / 'scripts'

# Read MO Avg Home Data
mo_home_data = data_processed / 'mo_10yr_avghomeval.csv'

# Create dataframe of MO average home val data
mo_df = pd.read_csv(mo_home_data)
print(mo_df)

# ----------------------------------------
# Clean to Only Last 10 Years of Data
# ----------------------------------------

# Convert 'YearEndData' to datetime b/c I forgot to filter for that on excel
mo_df['YearEndData'] = pd.to_datetime(mo_df['YearEndData'], format='%m/%d/%y')

# Get the latest year from the data
latest_year = mo_df['YearEndData'].dt.year.max()

# Filter for rows within the last 10 years
MOTenYearEndDF = mo_df[mo_df['YearEndData'].dt.year >= (latest_year - 9)]

# Clean up 'AverageHomeValue' column by removing $ and commas, then convert to float
MOTenYearEndDF['AverageHomeValue'] = (
    MOTenYearEndDF['AverageHomeValue']
    .replace('[\$,]', '', regex=True)
    .astype(float)
)

# Quick check
print(MOTenYearEndDF) # Keep MOTenYearEndDF per the instructions

# ----------------------------------------
# Data Analysis Steps for Missouri (MO)
# ----------------------------------------

# Subset series of home values
MOYearEndDatesSeries = MOTenYearEndDF['AverageHomeValue']

# Display the series
print("\nYear End Averages:")
print(MOYearEndDatesSeries)

# Print 3rd, 6th, and 9th values
print("\nThird year:", MOYearEndDatesSeries.iloc[2])
print("Sixth year:", MOYearEndDatesSeries.iloc[5])
print("Ninth year:", MOYearEndDatesSeries.iloc[8])

# Create custom row labels
row_labels = MOTenYearEndDF['YearEndData'].dt.strftime('MOYearEnd20%y')
MOTenYearEndDF.index = row_labels

# Print first, fifth, and last rows using custom labels
labels_list = MOTenYearEndDF.index.tolist()

print("\nFirst row:")
print(MOTenYearEndDF.loc[labels_list[0]])

print("\nFifth row:")
print(MOTenYearEndDF.loc[labels_list[4]])

print("\nLast row:")
print(MOTenYearEndDF.loc[labels_list[-1]])