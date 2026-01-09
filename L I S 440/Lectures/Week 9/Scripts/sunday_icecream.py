# Make sure to go to tools > download openpyxl to import
#   excel sheets directly but only doing csv for this

# Import the necessary packages
import pandas as pd
import os
from pathlib import Path


# --- Define base directories ---
# __file__ gives you the path of this script: /Week 9/Scripts/sunday_icecream.py
BASE_DIR = Path(__file__).resolve().parents[1]   # One level up → /Week 9

# Subfolders relative to the base directory
INPUT_DIR = BASE_DIR / "Input"
TEMP_DIR = BASE_DIR / "Temp"
OUTPUT_DIR = BASE_DIR / "Output"

# Fetch the ice cream data from temp folder
ice_cream_data = TEMP_DIR / "icecreamWeek_f25_AlejandroDeLaTorre.csv"

# --- Read data ---
df = pd.read_csv(ice_cream_data)

# Quick check to see that it loaded
print("Data loaded successfully!")
print(df.head())

# Now lets play with the data a bit
print(df) # to see the whole data since not that big
print(df.Cup) # Print the Cup column of the data

