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
# Analysis: Totals and Groupings
# ----------------------------------------

# Fetch the data
icecreamDF = pd.read_csv(data_processed / 'icecreamsales100random.csv')
print("\nIce Cream Data: ")
print(icecreamDF)


# Totals for All Transactions
print("Totals for All Transactions:")
totalScoops = icecreamDF['Scoops'].sum()
averageScoopSize = icecreamDF['Scoops'].mean()
print("Total Scoops (All Transactions):", totalScoops)
print("Average Scoop Size (All Transactions):", round(averageScoopSize, 2))

# Conditional Subsetting with Row Values
print("Conditional Subsetting: Flavor")

# Chocolate
chocolateDF = icecreamDF[icecreamDF['Flavor'] == 'Chocolate']
print("Chocolate Transactions:", chocolateDF.shape[0])
print("Chocolate Total Scoops:", chocolateDF['Scoops'].sum())
print("Chocolate Average Scoops:", round(chocolateDF['Scoops'].mean(), 2))

# Vanilla
vanillaDF = icecreamDF[icecreamDF['Flavor'] == 'Vanilla']
print("Vanilla Transactions:", vanillaDF.shape[0])
print("Vanilla Total Scoops:", vanillaDF['Scoops'].sum())
print("Vanilla Average Scoops:", round(vanillaDF['Scoops'].mean(), 2))

# Blue Moon
blueMoonDF = icecreamDF[icecreamDF['Flavor'] == 'Blue Moon']
print("Blue Moon Transactions:", blueMoonDF.shape[0])
print("Blue Moon Total Scoops:", blueMoonDF['Scoops'].sum())
print("Blue Moon Average Scoops:", round(blueMoonDF['Scoops'].mean(), 2))


print("Conditional Subsetting: Container")

# Waffle Cone
waffleDF = icecreamDF[icecreamDF['Container'] == 'WaffleCone']
print("Waffle Cone Transactions:", waffleDF.shape[0])
print("Waffle Cone Total Scoops:", waffleDF['Scoops'].sum())
print("Waffle Cone Average Scoops:", round(waffleDF['Scoops'].mean(), 2))

# Sugar Cone
sugarDF = icecreamDF[icecreamDF['Container'] == 'SugarCone']
print("Sugar Cone Transactions:", sugarDF.shape[0])
print("Sugar Cone Total Scoops:", sugarDF['Scoops'].sum())
print("Sugar Cone Average Scoops:", round(sugarDF['Scoops'].mean(), 2))

# Groupings
print("Groupings by Flavor:")
print("Transactions by Flavor:")
print(icecreamDF.groupby('Flavor').size())

print("Total Scoops by Flavor:")
print(icecreamDF.groupby('Flavor')['Scoops'].sum())

print("Average Scoops by Flavor:")
print(icecreamDF.groupby('Flavor')['Scoops'].mean().round(2))


print("Groupings by Container:")
print("Transactions by Container:")
print(icecreamDF.groupby('Container').size())

print("Total Scoops by Container:")
print(icecreamDF.groupby('Container')['Scoops'].sum())

print("Average Scoops by Container:")
print(icecreamDF.groupby('Container')['Scoops'].mean().round(2))