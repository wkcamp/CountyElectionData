import os
import textract

subcategories = { "1A": ["Clark",
                         "Columbiana",
                         "Erie",
                         "Geauga",
                         "Knox",
                         "Madison",
                         "Meigs",
                         "Preble",
                         "Ross"],
                  "1B": ["Allen",
                         "Monroe"],
                  "2A": ["Ashland",
                         "Defiance",
                         "Greene",
                         "Medina"],
                  "2B": ["Portage"],
                  "3A": ["Belmont",
                         "Huron"],
                  "3B": ["Guernsey"],
                  "4": ["Licking",
                        "Morrow",
                        "Paulding"],
                  "5": ["Miami", "Pike"],
                  "6": ["Summit"]
}

"""
categories = { "1": ["Allen",
                   "Clark",
                   "Columbiana",
                   "Erie",
                   "Geauga",
                   "Knox",
                   "Madison",
                   "Meigs",
                   "Monroe",
                   "Preble",
                   "Ross"],
               "2": ["Ashland",
                   "Defiance",
                   "Greene",
                   "Medina",
                   "Portage"],
               "3": ["Belmont",
                   "Guernsey",
                   "Huron"],
               "4": ["Licking",
                   "Morrow",
                   "Paulding"],
               "5": ["Miami", "Pike"],
               "6": ["Summit"]
}
"""

for category, counties in subcategories.iteritems():
    # Create a directory containing that county data
    path = "./processed/" + category
    os.mkdir(path)
    for county in counties:
        # Create a file with the county name
        text = textract.process("./data/" + county + ".pdf")
        # Output textract output into it
        processed_text_file = open(path + "/" + county + ".txt", "w")
        processed_text_file.write(text)
        processed_text_file.close()
