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


# [IGNORE] New dataframe Example
df = pd.DataFrame() # I don't like the arbitrarily long names Prof uses
print("Dimensions of this dataframe: ", df.shape)


# Read Student Data
student_data = data_processed / 'studentdatafile.csv'

# Create dataframe of student data
student_df = pd.read_csv(student_data)
# btw "\n" just puts it on newline
print("First 5 rows: \n", student_df.head()) # just show head
print("Last 5 rows: \n", student_df.tail()) # check if I am there


print("End of program.")


