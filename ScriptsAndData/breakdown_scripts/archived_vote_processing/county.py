class County:

    # Pattern recognition to determine: precincts, precincts identification number, and votes
    page_pattern = '^PAGE\s[0-9]+$'
    # Format for Precinct: "XXXX AZ - X", where X is a number and A,Z are letters
    precinct_pattern = '^[0-9]+\s[a-zA-Z]+[\s]*?[0-9a-zA-Z]+$'
    # Vote pattern is simply numbers
    vote_pattern = '^[0-9]+$'
    # Percent pattern is numbers with a percent sign and decimal
    percent_pattern = '^[0-9.%]+$'
    
    def get_sections(self):
        sections = []
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
                    sections.append((start, num))
                    # New section begins on the line after the page number.
                    start = num + 1
        return sections

    # If we match a precinct and the precincts flag is still False,
    # then we suppose this precinct is the initial one.
    def get_precinct(self, line):
        if re.match(precinct_pattern, line, line_num) is not None and precincts_flag is False:
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
        return precincts

    def get_votes(self, line):
         # The amount of precincts determines the amount of yes/no votes to collect
        num_votes = len(precincts)
        if re.match(vote_pattern, line) is not None and precincts_flag is True:
            # For a given padding N, the vote breakdown in each script
            # follows a list pattern such that the last item in that list
            # at the N - 1 is the total.
            # To check for a yes vote, we check
            # 1) The last N-1 votes were numbers, i.e. followed the vote pattern regex
            # 2) The yes flag is flipped.
            yes_flag = check_previous_votes(padding, line_num, file_lines, vote_pattern)

            # For a given file, the number of columns is important.
            # First, we need to keep track of columns within a precinct.
            # To do this, we use the "check_previous_vote" function above to
            # Ensure that a given vote meets the "previous" pattern commented above.
            # After that, we use our boolean from that function, call it yes_flag,
            # then check if yes_flag works, if the tracker of all the columns lines up with a
            # yes vote or no vote. Then we wipe the statements once we have finished the no votes.
            #
            # IF the column number is specified, then we figure out the yes/no votes.
            # How it works:
            # Keep track of the j-th column, we know that out of k columns,
            # when j = k - 1, that is the yes vote.
            # The j = k is the no vote.
        
            if yes_flag:
                col_counter += 1
                if col_counter == number_columns - 1:
                    yes_votes.append(line)
                elif col_counter == number_columns:
                    no_votes.append(line)
                    col_counter = 0
        

    # For a given padding N, checks if a pattern applies
    # for lines (line_num - N) to line_num
    def check_previous_votes(self, padding, line_num, lines, pattern):
        tracker = 0  # Tracks amount of matches within a set of lines
        start = line_num - padding + 1
        for index in range(start, line_num):
            if re.match(pattern, lines[index]) is not None:
                tracker += 1
        return tracker == padding - 1
    

    # Helper functions
    def __init__(self, county_name, group_id):
        self.county_name = county_name
        self.group_id = group_id
        self.file_path = self.__create_path()

    def __create_path(self):
        return = PROCESSED_PATH + self.group_id + "/" + self.county_name
