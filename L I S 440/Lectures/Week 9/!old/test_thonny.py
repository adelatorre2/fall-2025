import csv

with open('/Users/alexdelatorre/Library/CloudStorage/OneDrive-UW-Madison/Coursework/L I S 440/Lectures/Week 9/icecreamWeek_f25_AlejandroDeLaTorre.csv', 'r', newline='') as csvfile:
    # Create CSV Reader
    csv_reader = csv.reader(csvfile)
    
    for row in csv_reader:
        print(row)
        