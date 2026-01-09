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
# Grouping Tutorial: Ice Cream Sales
# ----------------------------------------

# Fetch the data
icecreamDF = pd.read_csv(data_processed / 'icecreamsales25.csv')
print("\nIce Cream Data: ")
print(icecreamDF)

# Fetch the Flavor Column
flavorColumn = icecreamDF["Flavor"]
print("Flavor Column:")
print(flavorColumn)

# Get just the chocolate of the flavor column
print()
chocolateRows = icecreamDF[ flavorColumn == "Chocolate" ]
print(chocolateRows)

# Now to sort by flavor:
print()
print("Sort and group by flavor")
flavorGrouping = icecreamDF.groupby("Flavor")
flavorGroupingTotals = flavorGrouping["Sale"].sum()
print(flavorGroupingTotals)






