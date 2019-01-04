import xlrd
import pandas

data_location = "./data/CountyLevys2015.xlsx"

workbook = xlrd.open_workbook(data_location)
# Extract first workbook sheet
data_sheet = workbook.sheet_by_index(0)

# Create a CSV file
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
    row_set = data_sheet.row_values(row)
    county_name = row_set[4]
    yes_votes = row_set[14]
    no_votes = row_set[15]
    type_referendum = row_set[5]
    referendum = row_set[6]
    if county_name not in excluded_counties:
        data = {"A": [county_name], "B": [yes_votes], "C": [no_votes]}
        df = pandas.DataFrame(data, columns=["A", "B", "C"])
        df.to_csv("./generated_data/" + county_name + "_" + referendum + ".csv")
