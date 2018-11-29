import re
import json

PROCESSED_PATH = "../processed/3A/"
counties_3A = ["Belmont", "Huron"]

for county in counties_3A:
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
            # TODO: Require section divider some way (?)
            
            # Format for Precinct: "XXXX AZ - X", where X is a number and A,Z are letters
            # precinct_pattern = '^[-]*?[0-9]+\s[a-zA-Z]+\s[-\s]*?[0-9]+$'
            precinct_pattern = '^[0-9]+\s[0-9]+[\s][.a-zA-Z0-9\s-]+$'
            result = re.match(precinct_pattern, line)
            # Collect the precincts
            if result is not None and result not in precincts:
                precinct = result.string
                # Collect all the precinct names
                precincts.append(precinct)
                # Assign the precinct a vote tally
                # First line after precinct is empty.
                next(f)
                # Second line is the yes vote
                yes_vote = next(f)
                # Third line after is empty
                next(f)
                # Fourth line after is the NO vote
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
            output_dest = "../json/3A/" + county + ".json"
            json_output = open(output_dest, "w")
            json_output.write(json_data)
            json_output.close()
