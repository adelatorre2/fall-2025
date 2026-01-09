
# Prof. Nyhoff's code...
import pandas
import matplotlib
from matplotlib import pyplot

#read data file into DF
print("read data file into DF...")
stateDataDF = pandas.read_csv("YearEndStates.csv")
print("stateDataDF:")
print(stateDataDF)
usd = "${:,.2f}"

print("\nSet Row Indexes to State Names...")
stateRowsDF = stateDataDF.set_index("State")
print("stateRowsDF:")
print(stateRowsDF)

# Selected State, All Years -- Bar Graph
print("\nSelected State, All Years -- Bar Graph...")
selectedState = "Wisconsin"
print("Selected State:", selectedState)
#Select State Row using .loc[]
print("Select State Row using .loc[] ...")
selectedStateRowSeries = stateRowsDF.loc[selectedState]
print("selectedStateRowSeries:")
print(selectedStateRowSeries)
#bar graph:
selectedStateRowSeries.plot(kind = "bar")
pyplot.title(selectedState + ", All Years")
pyplot.xlabel("Years")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()

# Selected Year, All States -- Bar Graph
print("\nSelected Year, All States -- Bar Graph...")
print("Select columns using subsetting with []...")
selectedYear = "2020"  # CHANGE THIS YEAR
print("Selected Year:", selectedYear)
allStatesRowsSelectedYearColumnSeries = stateRowsDF[selectedYear]
print("allStatesRowsSelectedYearColumnSeries:")
print(allStatesRowsSelectedYearColumnSeries)
#bar graph:
allStatesRowsSelectedYearColumnSeries.plot(kind = "bar")
pyplot.title(selectedYear + ", All States")
pyplot.xlabel("States")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()

# Selected State, Selected Years -- Bar Graph
print("\nSelected State, Selected Years -- Bar Graph...")
selectedState = "California"
print("Selected State:", selectedState)
# select columns using subsetting with [] :
print("Select columns using subsetting with []...")
selectedYearsList = ["2010", "2015", "2020"]
print("selectedYearsList:")
print(selectedYearsList)
selectedStateRowSelectedYearsSeries = selectedStateRowSeries[selectedYearsList]
print("selectedStateRowSelectedYearsSeries:")
print(selectedStateRowSelectedYearsSeries)
#bar graph:
selectedStateRowSelectedYearsSeries.plot(kind = "bar")
pyplot.title(selectedState + ", Selected Years" )
pyplot.xlabel("Selected Years")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()

# Selected States, All Years Clustered -- Bar Graph
print("\nSelected States, All Years Clustered -- Bar Graph...")
selectedStatesList = ["Wisconsin", "California"]
print("Selected States:", selectedStatesList)
#Select State Rows using .loc[]
print("Select State Rows using .loc[] ...")
selectedStatesRowsAllYearsDF = stateRowsDF.loc[selectedStatesList]
print("selectedStatesRowsAllYearsDF:")
print(selectedStatesRowsAllYearsDF)
#bar graph:
selectedStatesRowsAllYearsDF.plot(kind = "bar")
pyplot.title("Selected States, All Years")
pyplot.xlabel("Years")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()

# All Years, Selected States Clustered -- Bar Graph...
print("\nAll Years, Selected States Clustered -- Bar Graph...")
selectedStatesList = ["Wisconsin", "California"]
print("Selected States:", selectedStatesList)
#Select State Rows using .loc[]
print("Select State Rows using .loc[] ...")
selectedStatesRowsAllYearsDF = stateRowsDF.loc[selectedStatesList]
print("selectedStatesRowsDF:")
print(selectedStatesRowsAllYearsDF)
print("Transposing...")
allYearsRowsSelectedStatesDF = selectedStatesRowsAllYearsDF.transpose() 
print("allYearsRowsSelectedStatesDF:")
print(allYearsRowsSelectedStatesDF)
#bar graph:
allYearsRowsSelectedStatesDF.plot(kind = "bar")
pyplot.title("Selected States")
pyplot.title("All Years, Selected States")
pyplot.xlabel("Years")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()

# Three Selected States, Four Years Clustered -- Bar Graph...
print("\nTwo Selected States, Two Years Clustered -- Bar Graph...")
selectedStatesList = ["Wisconsin", "California", "Illinois"]
print("Selected States:", selectedStatesList)
#Select State Rows using .loc[]
print("Select State Rows using .loc[] ...")
selectedStatesRowsAllYearsDF = stateRowsDF.loc[selectedStatesList]
print("selectedStatesRowsAllYearsDF:")
print(selectedStatesRowsAllYearsDF)
# select columns using subsetting with [] :
print("Select columns using subsetting with []...")
selectedYearsList = ["2010", "2015", "2020", "2024" ]
print("selectedYearsList:")
print(selectedYearsList)
selectedStatesRowsSelectedYearsDF = selectedStatesRowsAllYearsDF[selectedYearsList]
print("selectedStatesRowsSelectedYearsDF:")
print(selectedStatesRowsSelectedYearsDF)
#bar graph:
selectedStatesRowsSelectedYearsDF.plot(kind = "bar")
pyplot.title("Selected States, Selected Years")
pyplot.xlabel("States")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()

# Four Selected Years, Three States Clustered -- Bar Graph...
print("\nFour Selected Years, Three States Clustered -- Bar Graph...")
selectedStatesList = ["Wisconsin", "California", "Illinois"]
print("Selected States:", selectedStatesList)
#Select State Rows using .loc[]
print("Select State Rows using .loc[] ...")
selectedStatesRowsAllYearsDF = stateRowsDF.loc[selectedStatesList]
print("selectedStatesRowsAllYearsDF:")
print(selectedStatesRowsAllYearsDF)
# select columns using subsetting with [] :
print("Select columns using subsetting with []...")
selectedYearsList = ["2010", "2015", "2020", "2024" ]
print("selectedYearsList:")
print(selectedYearsList)
selectedStatesRowsSelectedYearsDF = selectedStatesRowsAllYearsDF[selectedYearsList]
print("selectedStatesRowsSelectedYearsDF:")
print(selectedStatesRowsSelectedYearsDF)
selectedYearsRowsSelectedStatesDF = selectedStatesRowsSelectedYearsDF.transpose() 
print("selectedYearsRowsSelectedStatesDF:")
print(selectedYearsRowsSelectedStatesDF)
#bar graph:
selectedYearsRowsSelectedStatesDF.plot(kind = "bar")
pyplot.title("Selected Years, Selected States")
pyplot.xlabel("Years")
pyplot.ylabel("Average Single-Family Home Price (USD)")
pyplot.tight_layout()   # keeps labels from getting cut off
pyplot.show()








