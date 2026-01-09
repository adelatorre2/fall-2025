# Import the necessary packages
import pandas as pd
import os
from pathlib import Path

# Print version of pandas just for tracking purposes
print(pd.__version__)

# Because the professor does this
print("Alejandro De La Torre's Code...")

# Set current working directory (CWD) : root folder
root = Path(__file__).parent.parent.resolve()

# Show CWD
print("Current Working Directory: ",Path.cwd())

# Set CWD: Data
data = root / 'data'
# Set CWD: Data > Raw
data_raw = data / 'raw'
# Set CWD: Data > Processed
data_processed = root / 'data' / 'processed'
# Set CWD: Scripts
scripts = root / 'scripts'


# Read Randomized Ice Cream Data
icecream_data = data_processed / 'icecream_random.csv'

# Create dataframe of Ice Cream (IC) data
ic_df = pd.read_csv(icecream_data) # He labeled it wisconsinHousingDF but too long


# View first and last 3 entries for vibes
print("First 3 rows: \n", ic_df.head(3)) 
print("Last 3 rows: \n", ic_df.tail(3))


# Show and select the sugar column
sugar_col = ic_df['Sugar Cone']
print("Sugar Cone Sales:") # to print raw series data
print(sugar_col)

# Calculate total
print("Total Sugar Cone Sales:")
print(sugar_col.sum())

# Calculate largest (max)
print("Largest Sugar Cone Sales:")
print(sugar_col.max())

# Calculate smallest (min)
print("Smallest Sugar Cone Sales:") # Least? Minimum? Why smallest/largest?
print(sugar_col.min())

# Calculate count (of entries)
print("Number of Sugar Cone Sales Data Points:")
print(sugar_col.count())

# Calculate median
print("Median Sugar Cone Sales for All Flavors:")
print(sugar_col.median())

# Calculate average (mean)
print("Average Sugar Cone Sales for All Flavors:")
print(sugar_col.mean())
