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

# Path details for accessing processed text files
GROUP_NAME = "2A"
PROCESSED_PATH = "../processed/" + GROUP_NAME + "/"
FILE_NAME = "Ashland.txt"

# Pattern recognition to determine: precincts, precincts identification number, and votes
page_pattern = '^PAGE\s[0-9]+$'
# Format for Precinct: "XXXX AZ - X", where X is a number and A,Z are letters
precinct_pattern = '^[0-9]+\s[a-zA-Z]+[\s]*?[0-9a-zA-Z]+$'
# Vote pattern is simply numbers
vote_pattern = '^[0-9]+$'
# Percent pattern is numbers with a percent sign and decimal
percent_pattern = '^[0-9.%]+$'

## Initializers that collect data within a given file

# Sections[] stores a list of the starting and ending line of each page within a file
sections = []  # Stores dictionary of various sections
file_path = PROCESSED_PATH + FILE_NAME

## Process the sections within a given file.
with open(file_path, "r") as f:
    # Start marks the initial line number we read the file from.
    start = 0
    # This will enumerate a given line number and that line's
    # contents to determine if the contents indicate a new page
    for num, line in enumerate(f, start):
        # A new page matches  "page_pattern" ideally and
        # marks the end of the given section and begins
        # a new section after that.
        if re.match(page_pattern, line) is not None:
            # Add a tuple that indicates the start and end (which equals num in this case)
            # within the section list
            sections.append((start, num))
            # New section begins on the line after the page number.
            start = num + 1

## Grab each line's contents within a given file.
temp_file = open(file_path, "r")
file_lines = temp_file.readlines()
temp_file.close()

### Core processing aspect: iterate through a given section and process each line's contents

## Initializers for processing

# Data[] represents a set comprised of 4-tuples in which a given tuple
# appears as follows with four specified attributes:
# (section_number, precinct with id, yes votes, no votes)
data = []

# Precincts[] represents a set of precinct names within a given section.
precincts = []

# yes_votes[] represents a set of yes votes within a given section.
# no_votes[] represents the same thing, but for no votes.
yes_votes = []
no_votes = []


# Padding specifies how far apart the initial precincts are
padding = 4
# yes_vote_padding specifies how far apart a yes vote is from a percentage
yes_vote_padding = 1
# no_vote_padding specifies how far apart a yes vote is from its NO counterpart
no_vote_padding = 9

# Boolean flags to prevent overreaching in collecting a given attribute
precincts_flag = False

## Iteration to collect precincts

# Iterates through all the lines within file_lines[], keeping track of line number and the
# line's contents
for line_num, line in enumerate(file_lines):

    """
    Status at this point in the iteration: Collect precincts
    """
    
    # Remove '\n' character to make data readable.
    line = line.strip()

    # IMPORTANT: The following section will change line_num and line WITHIN
    # the file
    
    # If we match a precinct and the precincts flag is still False,
    # then we suppose this precinct is the initial one.
    if re.match(precinct_pattern, line) is not None and precincts_flag is False:

        while precincts_flag is False:
            if re.match(precinct_pattern, line) is not None:
                # Add the matched result to precincts[]
                precincts.append(line)
                # Move to the next line of interest
                line_num = line_num + padding + 1
                line = file_lines[line_num].strip()
            else:
                # If we find that the match, after a certain amount of padding is false
                precincts_flag = True

    """
    Status at this point in the iteration: Collect yes votes
    """
    # The amount of precincts determines the amount of yes/no votes to collect
    num_votes = len(precincts)
    if re.match(vote_pattern, line) is not None and precincts_flag is True:
        print "1st lvl exec"
        # For a vote to be considered YES, it must pass the following criteria:
        # 1) Match the vote pattern (i.e. be a number)
        # 2) X spaces, as specified by a vote-padding, after a number,
        #    must be a number with a percentage
        # 3) The line after the YES vote is empty

        # For a vote to be considered NO, it must
        # 1) Match the vote pattern (i.e. be a number)
        # 2) Be no_vote_padding away from a YES vote.
        # 3) The line after the NO vote is empty
        while len(yes_votes) != num_votes and len(no_votes) != num_votes:
            # has_percent_number determines whether a yes vote has a
            # percentage X spaces away.
            has_percentage_number = False
            if re.match(percent_pattern, file_lines[line_num + yes_vote_padding + 1]) is not None:
                has_percentage_number = True
            if (re.match(vote_pattern, line) is not None
                and has_percentage_number
                and file_lines[line_num+1] == ""):

                yes_votes.append[line]

                potential_new_line = line_num + no_vote_padding + 1
                potential_no_vote = file_lines[potential_new_line]
                space_after_no_vote = file_lines[potential_new_line + 1]
                if (re.match(vote_pattern, potential_no_vote) is not None
                    and space_after_no_vote == ""):
                    no_votes.append[potential_no_vote]
                    line_num = potential_new_line

    print yes_votes
    print no_votes
    print precincts
