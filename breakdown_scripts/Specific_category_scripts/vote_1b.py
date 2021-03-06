import re
PROCESSED_PATH = "../processed/1B/"
counties_1B = ["Allen", "Monroe"]
page_pattern = '^PAGE\s[0-9]+$'
precinct_id_pattern = '^\d\d\d\d+$'
precinct_name_pattern = '^[a-zA-Z]+\s[a-zA-Z]?[\sa-zA-Z]*?'
vote_pattern = '^[0-9]+$'
sections = []
for county in counties_1B:
    path = PROCESSED_PATH + county + ".txt"
    with open(path, "r") as f:
        # Identify sections
        start = 0
        for num, line in enumerate(f, start):
            if re.match(page_pattern, line) is not None:
                sections.append((start, num))
                start = num + 1
    # Open the file again to reset the position in reading the file
    temp_f = open(path, "r")
    # Split every line into its own.
    lines = temp_f.readlines()
    data = []
    for section_number, section in enumerate(sections):
        begin = section[0]
        end = section[1]
        ids_done = False
        ids_and_names_done = False
        yes_votes_not_done = True
        section_precincts_ids = []
        section_precincts_names = []
        section_yes_votes = []
        section_no_votes = []        
        for line_num, line in enumerate(lines):
            
            line = line.strip() # Remove '\n' character
            if begin <= line_num and line_num <= end:
                # From here, we collect our data
                if re.match(precinct_id_pattern, line) is not None:
                    # Store it
                    section_precincts_ids.append(line)
                    next2_line = lines[line_num + 2].strip()
                    if re.match(precinct_name_pattern, next2_line):
                        ids_done = True

                # There are three conditions in which we collect the precinct names
                # 1) If the object in question matches the precinct pattern regex
                # 2) If we are done collecting precincts' ID numbers
                # 3) If the list of precincts within a section is still less
                # than the precinct ids' list
                # (3) is important because we want to have equal list sizes to
                # obtain a 1-1 correspondence
                if (re.match(precinct_name_pattern, line) is not None
                    and ids_done
                    and len(section_precincts_names) < len(section_precincts_ids)):
                    section_precincts_names.append(line)
                    if (len(section_precincts_ids) > 0
                        and len(section_precincts_names) == len(section_precincts_ids)):
                        ids_and_names_done = True

                if ids_and_names_done and yes_votes_not_done:
                    if re.match(vote_pattern, line) is not None:
                        section_yes_votes.append(line)
                    if len(section_yes_votes) == len(section_precincts_names):
                        yes_votes_not_done = False

                if not yes_votes_not_done:
                    if re.match(vote_pattern, line) is not None:
                        section_no_votes.append(line)
                    if len(section_no_votes) == len(section_yes_votes):
                        # If this occurs, we've finished this section.
                        break
            # TODO
            # Format the data into an easier readable format
            # Probably something like p_id + p_name : [sect_num, sect_yes, sect_no]
            # Though this assumes that there is at most one referendum on the page
            if len(section_precincts_ids) > 0 and len(section_precincts_names) > 0:
                print section_precincts_ids
                print section_precincts_names
                print "=" * 60
            data.append([section_number, section_precincts_ids,
                         section_precincts_names, section_yes_votes, section_no_votes])
