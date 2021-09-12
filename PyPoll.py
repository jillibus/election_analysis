# The Election Analysis Pseudocode
# Collect the data
# 1. Load the data from resources/election_results.csv
# 2. The total number of votes cast
# 2. A complete list of candidates to received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. Close the file resources/election_results.csv

# Import dependencies
import csv
import datetime
import random
#import numpy

# Referencing File and opening it
# syntax: file_variable = open(file_name, mode) modes: (r)ead, (w)rite, 
#         e(x)clusive creation - it won't create one if not there, 
#         (a)ppend - will create the file if not there, otherwise it adds to the end,
#         (+) - open for read and write
#
"Assign a variable to the election_results.csv file"
file_to_load = 'resources/election_results.csv'

# (1) Open the election_results.csv file for read only
election_data = open(file_to_load,'r')

# Perform analysis


# Close the election_results.csv file
election_data.close()


