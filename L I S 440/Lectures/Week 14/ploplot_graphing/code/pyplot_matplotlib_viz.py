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

# Fetch the data
icecreamDF = pd.read_csv(data_processed / 'icecreamadditions.csv')
print("\nIce Cream Data: ")
print(icecreamDF)


# ============================
# GRAPH 1: All Flavors vs. All Containers
# ============================
print("\nGRAPH 1: All Flavors vs. All Containers...")
icecreamFlavorRowsDF = icecreamDF.set_index("Flavor")
print("icecreamFlavorRowsDF:")
print(icecreamFlavorRowsDF)


icecreamFlavorRowsDF.plot(kind="bar")
plt.title("All Flavors and All Containers")
plt.ylabel("Scoops")
plt.tight_layout()
plt.savefig(output / "graph1_all_flavors_all_containers_flavors_x.png")
plt.show()

# ============================
# GRAPH 2: All Containers vs. All Flavors
# ============================
print("\nGRAPH 2: All Containers vs. All Flavors...")
icecreamContainerRowsDF = icecreamFlavorRowsDF.transpose()
print("icecreamContainerRowsDF:")
print(icecreamContainerRowsDF)

icecreamContainerRowsDF.plot(kind="bar")
plt.title("All Containers and All Flavors")
plt.ylabel("Scoops")
plt.tight_layout()
plt.savefig(output / "graph2_all_containers_all_flavors_containers_x.png")
plt.show()

# ============================
# GRAPH 3: Missouri Flavor Pie Chart
# ============================
print("\nGRAPH 3: Missouri Pie Chart...")
selectedFlavor = "Missouri"
selectedFlavorSeries = icecreamFlavorRowsDF.loc[selectedFlavor]
print("selectedFlavorSeries:")
print(selectedFlavorSeries)

selectedFlavorSeries.plot(kind="pie", label="", autopct='%1.1f%%')
plt.title("Your State Favorite: Missouri")
plt.tight_layout()
plt.savefig(output / "graph3_missouri_pie_chart.png")
plt.show()

# ============================
# GRAPH 4: Missouri Bar Chart by Container
# ============================
print("\nGRAPH 4: Missouri Bar Chart by Container...")
selectedFlavorSeries.plot(kind="bar")
plt.title("Your State Favorite: Missouri - All Containers")
plt.ylabel("Scoops")
plt.tight_layout()
plt.savefig(output / "graph4_missouri_bar_chart.png")
plt.show()

# ============================
# GRAPH 5: Selected Flavors (Strawberry, Cookie Dough, Missouri) vs Selected Containers (SugarCone, CakeCone)
# ============================
print("\nGRAPH 5: Strawberry, Cookie Dough, Missouri vs. SugarCone and CakeCone (Flavors on x-axis)...")
selectedFlavorsList = ["Strawberry", "Cookie Dough", "Missouri"]
selectedContainersList = ["SugarCone", "CakeCone"]

selectedFlavorsDF = icecreamFlavorRowsDF.loc[selectedFlavorsList]
selectedFlavorsAndContainersDF = selectedFlavorsDF[selectedContainersList]
print("selectedFlavorsAndContainersDF:")
print(selectedFlavorsAndContainersDF)


selectedFlavorsAndContainersDF.plot(kind="bar")
plt.title("Selected Flavors and Containers")
plt.ylabel("Scoops")
plt.tight_layout()
plt.savefig(output / "graph5_selected_flavors_containers_flavors_x.png")
plt.show()

# ============================
# GRAPH 6: Selected Containers (SugarCone, CakeCone) vs Selected Flavors (Strawberry, Cookie Dough, Missouri)
# ============================
print("\nGRAPH 6: SugarCone and CakeCone vs. Strawberry, Cookie Dough, Missouri (Containers on x-axis)...")
selectedContainersDF = icecreamContainerRowsDF.loc[selectedContainersList]
selectedContainersAndFlavorsDF = selectedContainersDF[selectedFlavorsList]
print("selectedContainersAndFlavorsDF:")
print(selectedContainersAndFlavorsDF)

selectedContainersAndFlavorsDF.plot(kind="bar")
plt.title("Selected Containers and Flavors")
plt.ylabel("Scoops")
plt.tight_layout()
plt.savefig(output / "graph6_selected_containers_flavors_containers_x.png")
plt.show()