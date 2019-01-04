import tabula
import xlrd
import pandas

"""
This will create an EMPTY nested dictionary with the following structure:
{ County_name: {Referendum: [list of pages with referendum tabulated data]}, 
County_name2: ... }
"""
# First use Prof Meredith's Excel sheet with county and referendum data
data_location = "./data/CountyLevys2015.xlsx"

workbook = xlrd.open_workbook(data_location)
# Extract first workbook sheet
data_sheet = workbook.sheet_by_index(0)

# Create the base dictionary
referendum_data = {}

# Iterate through the excel sheet to obtain county and referendum names
for row in range(data_sheet.nrows):
    # Exclude the follow names:
    # Auglaize, Clermont, Crawford, Gallia, Harrison
    # Lucas, Mahoning, Marion, Morgan, Richland,
    # Sandusky, Shelby, Trumbull, Tuscarawas
    # Van Wert, Vinton, Williams
    excluded_counties = ["Auglaize", "Clermont", "Crawford", "Gallia",
                         "Lucas", "Mahoning", "Marion", "Morgan",
                         "Richland", "Sandusky", "Shelby", "Trumbull",
                         "Tuscarawas", "Van Wert", "Vinton", "Williams"]
    # Obtain a given row's values
    row_set = data_sheet.row_values(row)
    
    county_name = row_set[4]
    referendum = row_set[6]

    # Ensure the county name is not in the excluded list
    if county_name not in excluded_counties:
        referendum_data[county_name][referendum] = []

"""
With the dictionary now built, the nasty part is to manually determine which pages 
in which PDFs for each county are of interest. 
"""

for county in referendum_data:
    for referendum, pages in county.iteritems():
        print(referendum)
