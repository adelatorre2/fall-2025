# Import the necessary packages
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt  # Correct and consistent use

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
output = root / 'output' / 'figures'
output.mkdir(parents=True, exist_ok=True)  # Make sure output folder exists

# ----------------------------------------
# Demo [verbatim]
# ----------------------------------------

# Fetch the data
icecreamDF = pd.read_csv(data_processed / 'icecreamshort.csv')
print("\nIce Cream Data: ")
print(icecreamDF)

# ------------------------------
# Plot 1: Digits Line Plot
# ------------------------------
digitsList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nDigits List: ")
print(digitsList)
digitsSeries = pd.Series(digitsList)
print("Digit Series: ")
print(digitsSeries)

digitsSeries.plot(title="Digits Line Plot")
plt.savefig(output / 'figure_1.png')
plt.close()

# ------------------------------
# Plot 2: Ice Cream Bar Plot by Flavor
# ------------------------------
print("\nIceCream Data: ")
icecreamFlavorRowsDF = icecreamDF.set_index("Flavor")
print(icecreamFlavorRowsDF)

icecreamFlavorRowsDF.plot(kind="bar", title="Ice Cream Sales by Flavor & Container")
plt.tight_layout()
plt.savefig(output / 'figure_2.png')
plt.close()

# ------------------------------
# Plot 3: Transposed Bar Plot (Container on X)
# ------------------------------
print("\nIce Cream Data - Transposed: ")
icecreamContainersRowsDF = icecreamFlavorRowsDF.transpose()
print(icecreamContainersRowsDF)

icecreamContainersRowsDF.plot(kind="bar", title="Sales by Container Type (Transposed)")
plt.tight_layout()
plt.savefig(output / 'figure_3.png')
plt.close()

# ------------------------------
# Plot 4: Subset - Selected Flavors
# ------------------------------
print("\nSelected Flavors:")
selectedFlavors = ["Chocolate", "Vanilla"]
selectedFlavorsDF = icecreamContainersRowsDF[selectedFlavors]
print(selectedFlavorsDF)

selectedFlavorsDF.plot(kind="bar", title="Chocolate & Vanilla Sales by Container")
plt.tight_layout()
plt.savefig(output / 'figure_4.png')
plt.close()

# ------------------------------
# Plot 5: Pie Chart for Chocolate
# ------------------------------
print("\nSelected Flavor:")
selectedFlavor = "Chocolate"
selectedFlavorDF = icecreamContainersRowsDF[selectedFlavor]
print(selectedFlavorDF)

selectedFlavorDF.plot(kind="pie", title=f"{selectedFlavor} Sales Breakdown", autopct='%1.1f%%')
plt.ylabel('')  # remove y-label for clean pie chart
plt.tight_layout()
plt.savefig(output / 'figure_5.png')
plt.close()