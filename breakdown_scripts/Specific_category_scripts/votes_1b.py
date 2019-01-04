import re
import json

counties_1B = ["Allen", "Monroe"]
PROCESSED_PATH = "./processed/1B/"

for county in counties_1B:
    data = {}
    section_number = 0
    precincts = []
    precincts_numbers = []
    path = PROCESSED_PATH + county + ".txt"
    # Identity new sections by identification of "For the tax levy" and "Against..."
    section_pattern = '^PAGE\s[0-9]+$'
    precinct_number_pattern = '^[0-9]+$'
    precinct_pattern = '^[a-zA-Z]+[\s]*?[a-zA-Z]*?[0-9]*?'
    vote_pattern = '^[0-9]+$'
    # List of tuples with (beginning of section line number, end ")
    sections = []
    d = []
    with open(path, "r") as f:
        # Identify sections and lines with each section
        start = 1
        for num, line in enumerate(f, start):
            if increment_section_number(section_pattern, line):
                sections.append((start, num))
                # Start for the next section will be the next line.
                start = num + 1
        # For each section, find precincts id #, name, and yes vote and no vote
        f.seek(0)
        lines = f.readlines()
        got_precinct_numbers = False
        got_precinct_names = False
        got_yes_votes = False
        got_no_votes = False
        precincts_nums_sect = []
        precincts_names_sect = []
        precinct_yes_sect = []
        precinct_no_sect = []
        f.seek(0)
        for index, line in enumerate(lines):
            # Find which section we are in
            sect = belongs_to_section(index, sections)
            if not got_precinct_numbers:
                prec_number_result = re.match(precinct_number_pattern, line)
                print line
                if prec_number_result is not None:
                    print prec_number_result.string
                    precincts_nums_sect.append(prec_number_result.string)

            if not got_precinct_names:
                prec_name = re.match(precinct_pattern, line)
                if prec_name is not None:
                    # If we find a match with a precinct name, then we're past number sect
                    got_precinct_numbers = True
                    precincts_names_sect.append(prec_name.string)
                if len(precincts_names_sect) == len(precincts_nums_sect) and precincts_names_sect != 0:
                    got_precinct_names = True
            
            if not got_yes_votes:
                yes_votes = re.match(vote_pattern, line)
                if yes_votes is not None:
                    precinct_yes_sect.append(yes_votes.string)
                if len(precinct_yes_sect) == len(precincts_names_sect):
                    got_yes_votes = True

            if not got_no_votes:
                no_votes = re.match(vote_pattern, line)
                if no_votes is not None:
                    precinct_no_sect.append(no_votes.string)
                if len(precinct_no_sect) == len(precincts_names_sect):
                    got_no_votes = True                

            # Once everything is obtained, we align every precinct number with its corresponding
            # name, yes votes, and no votes
            if got_precinct_numbers and got_precinct_names and got_yes_votes and got_no_votes:
                for i, v in precinct_num_sect:
                    pcinct = str(precincts_nums_sect[i]) + " " + precincts_names_sect[i]
                    d.append((sect, pcinct, precinct_yes_sect[i], precinct_no_sect[i]))
                # Afterwards, reset everything
                got_precinct_numbers = False
                got_precinct_names = False
                got_yes_votes = False
                got_no_votes = False
                precinct_nums_sect = []
                precinct_names_sect = []
                precinct_yes_sect = []
                precinct_no_sect = []
    print d
    exit
