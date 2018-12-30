"""
This script serves to provide a generic way to process texts grouped like so:

Wanted Info
Unwanted
Unwanted
Wanted Info
Unwanted
Unwanted
etc...

To do this, this script takes an input "padding" which designates the space between the precinct names within a script. Once all precincts are collected, the script collects the first batch of yes votes and no votes and uses a 1-1 correspondence to align them.
"""
import re
import os

class County:

    ## Class variables
    
    # Pattern recognition to determine: precincts, precincts identification number, and votes
    page_pattern = '^PAGE\s[0-9]+$'
    # Format for Precinct: "XXXX AZ - X", where X is a number and A,Z are letters
    precinct_pattern = '^[0-9]+\s[a-zA-Z]+[\s]*?[0-9a-zA-Z]+$'
    # Vote pattern is simply numbers
    vote_pattern = '^[0-9]+$'
    # Percent pattern is numbers with a percent sign and decimal
    percent_pattern = '^[0-9.%]+$'
    
    def __init__(self, padding, number_of_columns, file_path):
        self.padding = padding
        self.number_of_columns = number_of_columns
        self.file_path = file_path
        ## Initialized county variables
        # File lines represents all the lines within a county's PDF
        self.file_lines = []
        # Data[] represents a set comprised of 4-tuples in which a given tuple
        # appears as follows with four specified attributes:
        # (section_number, precinct with id, yes votes, no votes)
        self.data = []
        # Precincts[] represents a set of precinct names within a given section.
        self.precincts = []
        # Sections represents a breakdown of the county PDF into sections by page
        self.sections = []
        # yes_votes[] represents a set of yes votes within a given section.
        # no_votes[] represents the same thing, but for no votes.
        self.yes_votes = []
        self.no_votes = []
        self.column_counter = 0
        self.precincts_flag = False
        # Used to switch b/w yes/no votes
        self.yes_vote_flag = True

    ## Function setters/getters

    def set_sections():
        ## Process the sections within a given file.
        with open(self.file_path, "r") as f:
            # Start marks the initial line number we read the file from.
            start = 0
            # This will enumerate a given line number and that line's
            # contents to determine if the contents indicate a new page
            for num, line in enumerate(f, start):
                # A new page matches  "page_pattern" ideally and
                # marks the end of the given section and begins
                # a new section after that.
                if re.match(page_pattern, line) is not None:
                    # Add a tuple that indicates the start and end
                    # (which equals num in this case)
                    # within the section list
                    self.sections.append((start, num))
                    # New section begins on the line after the page number.
                    start = num + 1

    def get_sections():
        return self.sections

    # Set and get file lines for a county
    def set_file_lines():
        temp_file = open(self.file_path, "r")
        file_lines = temp_file.readlines()
        temp_file.close()

    def get_file_lines():
        return self.file_lines

    # Specialized functions

    # For a given padding N, checks if a pattern applies
    # for lines (line_num - N) to line_num
    def check_previous_votes(padding, line_num, lines, pattern):
        tracker = 0  # Tracks amount of matches within a set of lines
        start = line_num - padding + 1
        for index in range(start, line_num):
            if re.match(pattern, lines[index]) is not None:
                tracker += 1
        return tracker == padding - 1
        
# Counties will be a list of county objects
for county in counties:
    county.set_sections()
    sections = county.get_sections()

    county.set_file_lines()
    file_lines = county.get_file_lines()

    # Iterates through all the lines within file_lines[],
    # keeping track of line number and the
    # line's contents
    for line_num, line in enumerate(county.file_lines):
            """
            Status at this point in the iteration: Collect precincts
            """
            # Remove '\n' character to make data readable.
            line = line.strip()

            # IMPORTANT: The following section will change line_num and line WITHIN
            # the file
    
            # If we match a precinct and the precincts flag is still False,
            # then we suppose this precinct is the initial one.
            if re.match(county.precinct_pattern, line) is not None and county.precincts_flag is False:
                while county.precincts_flag is False:
                    if re.match(county.precinct_pattern, line) is not None:
                        # Add the matched result to precincts[]
                        county.precincts.append(line)
                        # Move to the next line of interest
                        line_num = line_num + county.padding + 1
                        line = county.file_lines[line_num].strip()
                    else:
                        # If we find that the match, after a certain amount of padding is false
                        county.precincts_flag = True

            """
            Status at this point in the iteration: Collect yes votes
            """


            """ 
            Approach #1: Uses a flag to keep track of whereabouts in a file's voting scheme
            """
            # The amount of precincts determines the amount of yes/no votes to collect
            num_votes = len(precincts)
            if re.match(county.vote_pattern, line) is not None and county.precincts_flag is True:
                # For a given padding N, the vote breakdown in each script
                # follows a list pattern such that the last item in that list
                # at the N - 1 is the total.
                # To check for a yes vote, we check
                # 1) The last N-1 votes were numbers, i.e. followed the vote pattern regex
                # 2) The yes flag is flipped.
                county.yes_flag = county.check_previous_votes(county.padding, line_num,
                                                county.file_lines, county.vote_pattern)

                # For a given file, the number of columns is important.
                # First, we need to keep track of columns within a precinct.
                # To do this, we use the "check_previous_vote" function above to
                # Ensure that a given vote meets the "previous" pattern commented above.
                # After that, we use our boolean from that function, call it yes_flag,
                # then check if yes_flag works, if the tracker of all the columns lines up with a
                # yes vote or no vote. Then
                # we wipe the statements once we have finished the no votes.
                # IF the column number is specified, then we figure out the yes/no votes.
                # How it works:
                # Keep track of the j-th column, we know that out of k columns,
                # when j = k - 1, that is the yes vote.
                # The j = k is the no vote.
        
                if county.yes_flag:
                    county.column_counter += 1
                    if county.column_counter == county.number_columns - 1:
                        county.yes_votes.append(line)
                    elif county.column_counter == county.number_columns:
                        county.no_votes.append(line)
                        county.column_counter = 0
