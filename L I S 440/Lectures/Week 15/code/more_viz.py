# Import the necessary packages
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt

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

# Fetch the data
states_df = pd.read_csv(data_processed / 'YearEndStates.csv')
print("\n:Year End States Data:")
print(states_df)


# Set state and year lists
MO = "Missouri"
CA = "California"
IL = "Illinois"
ND = "North Dakota"

selected_states_3 = [MO, CA, IL]
selected_states_4 = [MO, CA, IL, ND]

years_3 = ["2010", "2015", "2020"]
years_4 = ["2010", "2015", "2020", "2024"]

# Set index to 'State'
states_df.set_index("State", inplace=True)


# ============================
# Graph 1: My State, All Years
# ============================
states_df.loc[MO].plot(kind="bar", title=f"{MO}, All Years")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph1_MO_all_years.png")
plt.close()

# ============================
# Graph 2: Another State, All Years
# ============================
states_df.loc[CA].plot(kind="bar", title=f"{CA}, All Years")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph2_CA_all_years.png")
plt.close()


# ============================
# Graph 3: All States, Year = 2009
# ============================
# I emailed professor Nyhoff to ask about why it says 2008 when data only goes back to 2009
states_df["2009"].plot(kind="bar", title="2009, All States")
plt.xlabel("States")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph3_all_states_2009.png")
plt.close()


# ============================
# Graph 4: All States, Year = 2020
# ============================
states_df["2020"].plot(kind="bar", title="2020, All States")
plt.xlabel("States")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph4_all_states_2020.png")
plt.close()

# ============================
# Graph 5: My State, Selected Years
# ============================
states_df.loc[MO, years_3].plot(kind="bar", title=f"{MO}, Selected Years")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph5_MO_selected_years.png")
plt.close()


# ============================
# Graph 6: Other State, Selected Years
# ============================
states_df.loc[CA, years_3].plot(kind="bar", title=f"{CA}, Selected Years")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph6_CA_selected_years.png")
plt.close()


# ============================
# Graph 7: Both States, All Years Clustered
# ============================
states_df.loc[[MO, CA]].transpose().plot(kind="bar", title="Selected States, All Years Clustered")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph7_both_states_all_years_clustered.png")
plt.close()

# ============================
# Graph 8: All Years, Both States Clustered
# ============================
ax = states_df.loc[[MO, CA]].plot(kind="bar", title="All Years, Selected States Clustered")
plt.xlabel("States")
plt.ylabel("Avg Home Price (USD)")
plt.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside plot
plt.tight_layout()
plt.savefig(output / "graph8_all_years_both_states_clustered.png", bbox_inches='tight')  # Adjust bounding box
plt.close()

# ============================
# Graph 9: 3 States x 4 Years Clustered
# ============================
states_df.loc[selected_states_3, years_4].transpose().plot(kind="bar", title="3 States x 4 Years Clustered")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph9_3_states_4_years.png")
plt.close()

# ============================
# Graph 10: 4 States x 3 Years Clustered
# ============================
states_df.loc[selected_states_4, years_3].transpose().plot(kind="bar", title="4 States x 3 Years Clustered")
plt.xlabel("Years")
plt.ylabel("Avg Home Price (USD)")
plt.tight_layout()
plt.savefig(output / "graph10_4_states_3_years.png")
plt.close()