# Import the necessary packages
import pandas as pd
import os
import pathlib

# Set working directory
path = r'/Users/alexdelatorre/Library/CloudStorage/OneDrive-UW-Madison/Coursework/L I S 440/Lectures/Week 10/Tuesday'
os.chdir(path)

print("Current Working Directory: ", os.getcwd())

# Read CSV
ice_cream_df = pd.read_csv('icecreamWeek_f25_AlejandroDeLaTorre.csv')

# Show shape of df
print("shape of our dataframe: ")
print( ice_cream_df.shape )
print("columns in our dataframe: ")
print( ice_cream_df.columns )

# Show first 5 rows
print("First five rows of data: ")
print( ice_cream_df.head() )

# Show first 3 rows
print("First three rows of data: ")
print( ice_cream_df.head(3) )



