import pandas as pd
import csv
import os


# Set working directory
cd = "

with open('/Users/alexdelatorre/Library/CloudStorage/OneDrive-UW-Madison/Coursework/L I S 440/Lectures/Week 9/icecreamWeek_f25_AlejandroDeLaTorre.csv', 'r', newline='') as csvfile:
    # Create CSV Reader
    csv_reader = csv.reader(csvfile)
    
    for row in csv_reader:
        print(row)
        
# If want to import .xlsx file do following:
# pip install pandas openpyxl
# file_path = '/Users/alexdelatorre/Library/CloudStorage/OneDrive-UW-Madison/Coursework/L I S 440/Lectures/Week 9/icecreamWeek_f25_AlejandroDeLaTorre.xlsx'
# df_xlsx = pd.read_excel(file_path, engine= 'openpyxl')

        
# Import CSV as dataframe under pandas

df = pd.read_csv()
