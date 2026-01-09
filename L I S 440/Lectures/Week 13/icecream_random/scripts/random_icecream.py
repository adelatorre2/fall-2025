# Import necessary packages
import pandas as pd
from pathlib import Path

# Print pandas version for tracking
print(pd.__version__)

# Personal tag
print("Alejandro De La Torre's Code...")

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
scripts = root / 'scripts'

# Define path to CSV file
icecream_csv = data_processed / 'icecream_random.csv'

# Load CSV into DataFrame
ic_df = pd.read_csv(icecream_csv)

# Preview data
print("First 3 rows:\n", ic_df.head(3))
print("Last 3 rows:\n", ic_df.tail(3))

# -------------------------------
# Total scoops across all containers
# -------------------------------

# Calculate total scoops per flavor across all columns except 'Flavor'
ic_df['Total Scoops (All Containers)'] = ic_df.iloc[:, 1:].sum(axis=1)

# Display results
print("\nTotal Scoops for Each Flavor Across All Containers:")
print(ic_df[['Flavor', 'Total Scoops (All Containers)']])

# -------------------------------
# Total scoops for selected containers only
# -------------------------------

# Define selected container columns
selected_containers = ['Waffle Cone', 'Cake Cone', 'Pretzel Cone']

# Calculate total scoops per flavor for selected containers
ic_df['Total Scoops (Selected Containers)'] = ic_df[selected_containers].sum(axis=1)

# Display results
print("\nTotal Scoops for Each Flavor for Waffle Cone, Cake Cone, and Pretzel Cone:")
print(ic_df[['Flavor', 'Total Scoops (Selected Containers)']])

