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
icecream_data = data_processed / 'icecreamWeek_sp25_AlejandroDeLaTorre.csv'

# Create dataframe of Ice Cream (IC) data
ic_df = pd.read_csv(icecream_data) 
print(ic_df)

# Define lables for rows
rowLabels = ["choc", "straw", "van", "bmoon", "orng", "chry", "cdough"]

# View first and last 3 entries for vibes
print("First 3 rows: \n", ic_df.head(3)) 
print("Last 3 rows: \n", ic_df.tail(3))

print()
print("New row labels:")
print(rowLabels)
ic_df.index = rowLabels
print()
print("Reindexed data frame:")
print(ic_df)

flavorSeries = ic_df["Flavors"]
print()
print ("Flavor series:")
print (flavorSeries)

sortedFlavorSeries = flavorSeries.sort_values()
print()
print("Sorted Flavor Series:")
print(sortedFlavorSeries)

print()
sugarConeSeries = ic_df["Sugar Cone"]
print("sugarConeSeries:")
print(sugarConeSeries)

print()
chocolateRow = ic_df.iloc[0]
print("Chocolate Row:")
print(chocolateRow)

print()
VanillaRow = ic_df.loc["van"]
print("Vanilla Row:")
print(VanillaRow)

print()
VanillaRow = ic_df.iloc[2]
print("Vanilla Row:")
print(VanillaRow)

print()
cupSeries = ic_df["Cup"]
print("Cup Sales")
print(cupSeries)
print("Cup Strawberry Sales:")
cupStrawberrySales = cupSeries.iloc[1]
print(cupStrawberrySales)
cupStrawberrySales = cupSeries.loc["straw"]
print(cupStrawberrySales)

cones_df = ic_df[ ["Sugar Cone", "Waffle Cone"]   ]
print()
print("Cones Sales, Sugar and Waffle:")
print(cones_df)

cones_col = ["Sugar Cone", "Waffle Cone"]
print()
print("Cone columns:")
print(cones_col)
cones_dfic_df = ic_df[ cones_col ]
print("Cone Sales:")
print(cones_df)