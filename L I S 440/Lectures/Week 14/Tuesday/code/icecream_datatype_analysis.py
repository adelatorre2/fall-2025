# Import the necessary packages
import pandas as pd
import os
from pathlib import Path

# Print version of pandas
print("Alejandro De La Torre's code....")
print(pd.__version__)


# ----------------------------------------
# File & Path Setup
# ----------------------------------------

# Set root directory (two levels up from this script)
root = Path(__file__).parent.parent.resolve()

# Show current working directory
print("Current Working Directory:", Path.cwd())

# Define key directories
data = root / 'data'
data_raw = data / 'raw'
data_processed = data / 'processed'
output = root / 'output'
code = root / 'code'


# ----------------------------------------
# Data Cleaning
# ----------------------------------------

# Fetch the data
icecreamDF = pd.read_csv(data_processed / 'icecreamNA.csv')
print() # return
print("Ice Cream Data: ")
print(icecreamDF)

# Use this method to drop NA values
# print()
# print("Drop NA Data:")
# icecreamCleanDF = icecreamDF.dropna() # to drop N/A values

# Fill the NA values with 0 
print()
print("Zero Out the NA data:")
icecreamCleanDF = icecreamDF.fillna(0)
print(icecreamCleanDF)
# If want to overwrite the original df directly just
# icecreamDF.fillna(0, inplace=True)

# Method to check for NA data
print()
print("Look for NA data:")
icecreamNAvaluesDF = icecreamDF.isna()
print(icecreamNAvaluesDF)

# We can inspect the total NA values...
print()
print("Total NA values:")
totalNAValues = icecreamNAvaluesDF.sum()
print(totalNAValues)

# Alternatively we can combine the check and inspect steps
print()
print("Total NA values (method chaining)")
totalNAvalues =icecreamDF.isna().sum()
print(totalNAvalues)

