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

# Fetch the data
ic_df = pd.read_csv(data_processed / 'icecream_random.csv')
print("\n:Random Ice Cream data:")
print(ic_df)

# --------------------------------------------------------
# Sugar Cone Stats
# --------------------------------------------------------
print("\nSugar Cone Sales:")
sugar = ic_df["Sugar Cone"]
print(sugar)

print("\nTotal Sugar Cone Sales:")
print(sugar.sum())

print("\nLargest Sugar Cone Sale:")
print(sugar.max())

print("\nSmallest Sugar Cone Sale:")
print(sugar.min())

print("\nNumber of Sugar Cone Sales Data Points:")
print(sugar.count())

print("\nMedian Sugar Cone Sales for All Flavors:")
print(sugar.median())

print("\nAverage Sugar Cone Sales for All Flavors:")
print(sugar.mean())


# --------------------------------------------------------
# Cup Stats
# --------------------------------------------------------
print("\nCup Sales:")
cup = ic_df["Cup"]
print(cup)

print("\nTotal Cup Sales:")
print(cup.sum())

print("\nLargest Cup Sale:")
print(cup.max())

print("\nSmallest Cup Sale:")
print(cup.min())

print("\nNumber of Cup Sales Data Points:")
print(cup.count())

print("\nMedian Cup Sales for All Flavors:")
print(cup.median())

print("\nAverage Cup Sales for All Flavors:")
print(cup.mean())


# --------------------------------------------------------
# Waffle Cone Stats
# --------------------------------------------------------
print("\nWaffle Cone Sales:")
waffle = ic_df["Waffle Cone"]
print(waffle)

print("\nTotal Waffle Cone Sales:")
print(waffle.sum())

print("\nLargest Waffle Cone Sale:")
print(waffle.max())

print("\nSmallest Waffle Cone Sale:")
print(waffle.min())

print("\nNumber of Waffle Cone Sales Data Points:")
print(waffle.count())

print("\nMedian Waffle Cone Sales for All Flavors:")
print(waffle.median())

print("\nAverage Waffle Cone Sales for All Flavors:")
print(waffle.mean())


# --------------------------------------------------------
# Cake Cone Stats
# --------------------------------------------------------
print("\nCake Cone Sales:")
cake = ic_df["Cake Cone"]
print(cake)

print("\nTotal Cake Cone Sales:")
print(cake.sum())

print("\nLargest Cake Cone Sale:")
print(cake.max())

print("\nSmallest Cake Cone Sale:")
print(cake.min())

print("\nNumber of Cake Cone Sales Data Points:")
print(cake.count())

print("\nMedian Cake Cone Sales for All Flavors:")
print(cake.median())

print("\nAverage Cake Cone Sales for All Flavors:")
print(cake.mean())


# --------------------------------------------------------
# Pretzel Cone Stats
# --------------------------------------------------------
print("\nPretzel Cone Sales:")
pretzel = ic_df["Pretzel Cone"]
print(pretzel)

print("\nTotal Pretzel Cone Sales:")
print(pretzel.sum())

print("\nLargest Pretzel Cone Sale:")
print(pretzel.max())

print("\nSmallest Pretzel Cone Sale:")
print(pretzel.min())

print("\nNumber of Pretzel Cone Sales Data Points:")
print(pretzel.count())

print("\nMedian Pretzel Cone Sales for All Flavors:")
print(pretzel.median())

print("\nAverage Pretzel Cone Sales for All Flavors:")
print(pretzel.mean())