import re
import json

def pattern_matches(section_pattern, line):
    return True if re.match(section_pattern, line) is not None else False

def increment_section_number(section_pattern, line):
    is_section = pattern_matches(section_pattern, line)
    return is_section

def belongs_to_section(index, sections):
    for j, (start, end) in enumerate(sections):
        if start <= index and index <= end:
            return j
# Sample text with Clark Data:
PROCESSED_PATH = "./processed/1B/"
counties_1A = ["Clark",
               "Columbiana",
               "Erie",
               "Geauga",
               "Knox",
               "Madison",
               "Meigs",
               "Preble",
               "Ross"]
counties_1B = ["Allen", "Monroe"]
counties_2A = ["Ashland", "Defiance", "Greene", "Medina"]
counties_2B = ["Portage"]
counties_3A = ["Belmont", "Huron"]
counties_4 = ["Licking", "Morrow", "Paulding"]
counties_5 = ["Miami", "Pike"]
counties_6 = ["Summit"]
"""
for county in counties_1A:
    # Initializers:
    # data: stores all the precincts and voting information attached to them
    # Section_number: keeps track of which section within the output we are in
    # Precincts: contains the entire list of precincts for a given county
    data = {}
    section_number = 0
    precincts = []

    # Processed data are stored within the processed path as text files
    path = PROCESSED_PATH + county + ".txt"
    with open(path, "r") as f:
        for line in f:
            # Format for a new section: "=" * X where X is a number >= 1
            section_pattern = '^[=]+$'
            is_section = True if re.match(section_pattern, line) is not None else False
            if is_section:
                # If we find out that we're within a new section, then we increment the
                # counter by one
                section_number += 1
            # Format for Precinct: "XXXX AZ - X", where X is a number and A,Z are letters
            precinct_pattern = '^[-]*?[0-9]+\s[a-zA-Z]+\s[-\s]*?[0-9]+$'
            result = re.match(precinct_pattern, line)
            # Collect the precincts
            if result is not None and result not in precincts:
                precinct = result.string
                # Collect all the precinct names
                precincts.append(precinct)
                # Assign the precinct a vote tally
                # First line after is the YES vote
                yes_vote = next(f)
                # Second line after is the NO vote
                no_vote = next(f)

                # We use section numbers to keep track of the "=" in the data.
                precinct_name = precinct.strip()
                vote_data = [section_number, yes_vote.strip(), no_vote.strip()]
                if precinct_name not in data:
                    # Initial set for voting
                    data[precinct_name] = [vote_data]
                else:
                    # Append the data, if it is not the initial set
                    data[precinct_name].append(vote_data)

                    # Encode the data within a JSON format to store it.
            json_data = json.dumps(data)
            output_dest = "./json/1A/" + county + ".json"
            json_output = open(output_dest, "w")
            json_output.write(json_data)
            json_output.close()
"""

