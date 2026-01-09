# Import the necessary packages
import pandas as pd # because 6 characters is to much
import os
from pathlib import Path # to set up paths easier

# Print version of pandas
print(pd.__version__)

# Set working directory (CWD) : root folder
root = Path(__file__).parent.parent.resolve()

# Show current working directory
print("Current Working Directory: ",Path.cwd())

# Set CWD: Data
data = root / 'data'
# Set CWD: Data > Raw
data_raw = data / 'raw'
# Set CWD: Data > Processed
data_processed = root / 'data' / 'processed'
# Set CWD: Scripts
scripts = root / 'scripts'


# Read Student Data
icecream_data = data_processed / 'icecream_random.csv'

# Create dataframe of student data
ic_df = pd.read_csv(icecream_data) # He labeled it wisconsinHousingDF but too long


# View first and last 3 entries
print("First 5 rows: \n", ic_df.head(3)) # just show head
print("Last 5 rows: \n", ic_df.tail(3)) # check if I am there